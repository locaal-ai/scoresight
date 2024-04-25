from os import path
import cv2
from tesserocr import PyTessBaseAPI, RIL, iterate_level
import numpy as np
from PIL import Image
from defaults import FieldType
from storage import fetch_data
from text_detection_target import TextDetectionTarget, TextDetectionTargetWithResult
import re
from PySide6.QtCore import QRectF
from threading import Lock


def autocrop(image_in):
    image = image_in.copy()
    # check if this image is black-on-white or white-on-black by looking at the first few pixels
    if np.sum(image[0:5, 0:5]) > 0:
        # black-on-white
        # invert the image
        image = 255 - image

    # find the first row that has a pixel
    first_row = 0
    for row in range(image.shape[0]):
        if np.sum(image[row, :]) > 0:
            first_row = row
            break
    # find the last row that has a pixel
    last_row = image.shape[0] - 1
    for row in range(image.shape[0] - 1, -1, -1):
        if np.sum(image[row, :]) > 0:
            last_row = row
            break
    # find the first column that has a pixel
    first_col = 0
    for col in range(image.shape[1]):
        if np.sum(image[:, col]) > 0:
            first_col = col
            break
    # find the last column that has a pixel
    last_col = image.shape[1] - 1
    for col in range(image.shape[1] - 1, -1, -1):
        if np.sum(image[:, col]) > 0:
            last_col = col
            break
    # leave a 10 pixel border on each side
    first_row = max(0, first_row - 10)
    last_row = min(image.shape[0] - 1, last_row + 10)
    first_col = max(0, first_col - 10)
    last_col = min(image.shape[1] - 1, last_col + 10)
    return image_in[first_row:last_row, first_col:last_col], (
        first_row,
        last_row,
        first_col,
        last_col,
    )


def add_ordinal_indicator(text):
    if text == "":
        return ""
    if text.endswith("1") and text != "11":
        return text + "st"
    elif text.endswith("2") and text != "12":
        return text + "nd"
    elif text.endswith("3") and text != "13":
        return text + "rd"
    else:
        return text + "th"


def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


class TextDetectionResult:
    def __init__(self, text, state, rect=None, extra=None):
        self.text = text
        self.state = state
        self.rect = rect
        self.extra = extra


class TextDetector:
    # model name enum: daktronics=0, scoreboard_general=1
    class OcrModelIndex:
        DAKTRONICS = 0
        SCOREBOARD_GENERAL = 1
        GENERAL_ENGLISH = 2
        SCOREBOARD_GENERAL_LARGE = 3

    class BinarizationMethod:
        GLOBAL = 0
        NO_BINARIZATION = 1
        LOCAL = 2
        ADAPTIVE = 3

    def __init__(self):
        self.api_lock = Lock()
        self.api = None
        if (
            fetch_data(
                "scoresight.json",
                "ocr_model",
                TextDetector.OcrModelIndex.SCOREBOARD_GENERAL,
            )
            == TextDetector.OcrModelIndex.SCOREBOARD_GENERAL
        ):
            self.setOcrModel(TextDetector.OcrModelIndex.SCOREBOARD_GENERAL)
        else:
            self.setOcrModel(TextDetector.OcrModelIndex.DAKTRONICS)

    def setOcrModel(self, ocrModelIndex):
        ocr_model = None
        if ocrModelIndex == self.OcrModelIndex.DAKTRONICS:
            ocr_model = "daktronics"
        if ocrModelIndex == self.OcrModelIndex.SCOREBOARD_GENERAL:
            ocr_model = "scoreboard_general"
        if ocrModelIndex == self.OcrModelIndex.GENERAL_ENGLISH:
            ocr_model = "eng"
        if ocrModelIndex == self.OcrModelIndex.SCOREBOARD_GENERAL_LARGE:
            ocr_model = "scoreboard_general_large"
        if ocr_model is None:
            return

        with self.api_lock:
            if self.api is not None:
                self.api.End()
                self.api = None
            self.api = PyTessBaseAPI(
                path=path.abspath(
                    path.join(path.dirname(__file__), "tesseract/tessdata")
                ),
                lang=ocr_model,
            )
            # single word PSM
            self.api.SetPageSegMode(8)
            self.api.SetVariable("load_system_dawg", "F")
            self.api.SetVariable("load_freq_dawg", "F")

    def detect_text(self, image):
        if image is None:
            return ""
        if not isinstance(image, np.ndarray):
            return ""
        # check the image has rows and columns
        if len(image.shape) < 2 or image.shape[0] < 1 or image.shape[1] < 1:
            return ""
        pilimage = Image.fromarray(image)
        text = ""
        with self.api_lock:
            self.api.SetImage(pilimage)
            text = self.api.GetUTF8Text()
        return text.strip()

    def detect_multi_text(
        self, binary, gray, rects: list[TextDetectionTarget], multi_crop=False
    ) -> list[TextDetectionResult]:
        if binary is None:
            return []
        if not isinstance(binary, np.ndarray):
            return []
        # check the image has rows and columns
        if len(binary.shape) < 2 or binary.shape[0] < 1 or binary.shape[1] < 1:
            return []

        if not multi_crop:
            pilimage = Image.fromarray(binary)
            with self.api_lock:
                self.api.SetImage(pilimage)

        texts = []
        for rect in rects:
            effectiveRect = None
            scale_x = 1.0
            scale_y = 1.0
            if multi_crop:
                if (
                    rect.x() < 0
                    or rect.y() < 0
                    or rect.width() < 1
                    or rect.height() < 1
                ):
                    texts.append(
                        TextDetectionResult(
                            "", TextDetectionTargetWithResult.ResultState.Empty, None
                        )
                    )
                    continue

                if rect.x() + rect.width() > binary.shape[1]:
                    rect.setWidth(binary.shape[1] - rect.x())
                if rect.y() + rect.height() > binary.shape[0]:
                    rect.setHeight(binary.shape[0] - rect.y())

                if (
                    rect.settings is not None
                    and "binarization_method" in rect.settings
                    and rect.settings["binarization_method"]
                    != TextDetector.BinarizationMethod.GLOBAL
                ):
                    if (
                        rect.settings["binarization_method"]
                        == TextDetector.BinarizationMethod.NO_BINARIZATION
                    ):
                        # no binarization
                        imagecrop = gray[
                            int(rect.y()) : int(rect.y() + rect.height()),
                            int(rect.x()) : int(rect.x() + rect.width()),
                        ]
                    elif (
                        rect.settings["binarization_method"]
                        == TextDetector.BinarizationMethod.LOCAL
                    ):
                        # local binarization using Otsu's method
                        _, imagecrop = cv2.threshold(
                            gray[
                                int(rect.y()) : int(rect.y() + rect.height()),
                                int(rect.x()) : int(rect.x() + rect.width()),
                            ],
                            0,
                            255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
                        )
                    elif (
                        rect.settings["binarization_method"]
                        == TextDetector.BinarizationMethod.ADAPTIVE
                    ):
                        # apply adaptive binarization
                        imagecrop = cv2.adaptiveThreshold(
                            gray[
                                int(rect.y()) : int(rect.y() + rect.height()),
                                int(rect.x()) : int(rect.x() + rect.width()),
                            ],
                            255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY,
                            # use a fraction of the patch area
                            max(int(rect.width() * rect.height() * 0.01), 3) | 1,
                            2,
                        )
                    # update the binary image for visualisation in the binary mode
                    binary[
                        int(rect.y()) : int(rect.y() + rect.height()),
                        int(rect.x()) : int(rect.x() + rect.width()),
                    ] = imagecrop
                else:
                    imagecrop = binary[
                        int(rect.y()) : int(rect.y() + rect.height()),
                        int(rect.x()) : int(rect.x() + rect.width()),
                    ]

                if (
                    rect.settings is not None
                    and "cleanup_thresh" in rect.settings
                    and rect.settings["cleanup_thresh"] > 0
                ):
                    # cleanup image from small components: find contours and remove small ones
                    contours, _ = cv2.findContours(
                        imagecrop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
                    )
                    # cleanup_thresh is [0, 1.0], convert to [0, 0.05]
                    cleanup_thresh = rect.settings["cleanup_thresh"] * 0.05
                    img_area_thresh = (
                        imagecrop.shape[0] * imagecrop.shape[1] * cleanup_thresh
                    )
                    for contour in contours:
                        if cv2.contourArea(contour) < img_area_thresh:
                            cv2.drawContours(imagecrop, [contour], 0, 0, -1)

                if (
                    rect.settings is not None
                    and "vscale" in rect.settings
                    and rect.settings["vscale"] != 10
                ):
                    # vertical scale the image
                    # the vscale input is in the range [1, 10] where 10 is the default (1:1)
                    # scale the image in the y direction about the center
                    rows, cols = imagecrop.shape
                    # calculate the target height
                    target_height = int(rows * (rect.settings["vscale"] / 10.0))
                    scaled = cv2.resize(
                        imagecrop, (cols, target_height), 0, 0, cv2.INTER_AREA
                    )
                    # add padding to the top and bottom
                    pad_top = (rows - target_height) // 2
                    pad_bottom = rows - target_height - pad_top
                    scaled = cv2.copyMakeBorder(
                        scaled, pad_top, pad_bottom, 0, 0, cv2.BORDER_REPLICATE
                    )
                    # make sure the image is the same size as the original
                    scaled = scaled[:rows, :]
                    # copy back into imagecrop and binary display
                    binary[
                        int(rect.y()) : int(rect.y() + rect.height()),
                        int(rect.x()) : int(rect.x() + rect.width()),
                    ] = scaled
                    imagecrop = scaled

                if (
                    rect.settings is not None
                    and "skew" in rect.settings
                    and rect.settings["skew"] != 0
                ):
                    # skew the image in the x direction about the center
                    rows, cols = imagecrop.shape
                    # identity 2x2 matrix
                    M = np.float32([[1, 0, 0], [0, 1, 0]])
                    # add skew factor to matrix
                    M[0, 1] = rect.settings["skew"] / 40.0
                    try:
                        skewed = cv2.warpAffine(imagecrop, M, (cols, rows))
                        binary[
                            int(rect.y()) : int(rect.y() + rect.height()),
                            int(rect.x()) : int(rect.x() + rect.width()),
                        ] = skewed
                        imagecrop = skewed
                    except:
                        pass

                if (
                    rect.settings is not None
                    and "dilate" in rect.settings
                    and rect.settings["dilate"] > 0
                    and imagecrop.shape[0] > 0
                    and imagecrop.shape[1] > 0
                ):
                    # dilate the image
                    kernel = np.ones((3, 3), np.uint8)
                    dilated = cv2.dilate(
                        imagecrop.copy(),
                        kernel,
                        iterations=int(rect.settings["dilate"]),
                    )
                    # copy back into image crop
                    binary[
                        int(rect.y()) : int(rect.y() + rect.height()),
                        int(rect.x()) : int(rect.x() + rect.width()),
                    ] = dilated

                if (
                    rect.settings is not None
                    and "invert_patch" in rect.settings
                    and rect.settings["invert_patch"]
                ):
                    # invert the image
                    imagecrop = 255 - imagecrop

                if (
                    rect.settings is not None
                    and "skip_similar_image" in rect.settings
                    and rect.settings["skip_similar_image"]
                ):
                    # compare the image with the last image
                    if (
                        rect.last_image is not None
                        and rect.last_image.shape == imagecrop.shape
                    ):
                        # check if the difference is less than 5%
                        diff = cv2.absdiff(rect.last_image, imagecrop)
                        diff = diff.astype(np.float32)
                        diff = diff / 255.0
                        diff = diff.sum() / (imagecrop.shape[0] * imagecrop.shape[1])
                        if diff < 0.05:
                            # skip this image
                            texts.append(
                                TextDetectionResult(
                                    "SIM",
                                    TextDetectionTargetWithResult.ResultState.FailedFilter,
                                    effectiveRect,
                                )
                            )
                            continue
                    rect.last_image = imagecrop.copy()

                if (
                    rect.settings is not None
                    and "autocrop" in rect.settings
                    and rect.settings["autocrop"]
                ):
                    # auto crop the binary image around the text
                    imagecrop, (first_row, last_row, first_col, last_col) = autocrop(
                        imagecrop
                    )
                    effectiveRect = QRectF(
                        first_col,
                        first_row,
                        last_col - first_col,
                        last_row - first_row,
                    )

                # check if image is size 0
                if imagecrop.shape[0] == 0 or imagecrop.shape[1] == 0:
                    texts.append(
                        TextDetectionResult(
                            "",
                            TextDetectionTargetWithResult.ResultState.Empty,
                            effectiveRect,
                        )
                    )
                    continue

                if (
                    rect.settings is not None
                    and "rescale_patch" in rect.settings
                    and rect.settings["rescale_patch"]
                ):
                    # rescale the image to 35 pixels height
                    scale_x = 35 / imagecrop.shape[0]
                    scale_y = scale_x

                if (
                    rect.settings is not None
                    and "normalize_wh_ratio" in rect.settings
                    and rect.settings["normalize_wh_ratio"]
                    and "median_wh_ratio" in rect.settings
                    and rect.settings["median_wh_ratio"] > 0
                ):
                    # rescale the image in x or in y such that the width-to-height ratio is 0.5
                    scale_x *= 0.5 / rect.settings["median_wh_ratio"]

                if scale_x != 1.0 or scale_y != 1.0:
                    imagecrop = cv2.resize(
                        imagecrop,
                        None,
                        fx=scale_x,
                        fy=scale_y,
                        interpolation=cv2.INTER_AREA,
                    )

                try:
                    pilimage = Image.fromarray(imagecrop)
                    with self.api_lock:
                        self.api.SetImage(pilimage)
                except:
                    texts.append(
                        TextDetectionResult(
                            "", TextDetectionTargetWithResult.ResultState.Empty, None
                        )
                    )
                    continue

            if rect.settings["type"] == FieldType.NUMBER:
                with self.api_lock:
                    self.api.SetVariable("tessedit_char_whitelist", "0123456789")
            elif rect.settings["type"] == FieldType.TIME:
                with self.api_lock:
                    self.api.SetVariable("tessedit_char_whitelist", "0123456789:.")
            else:  # general
                with self.api_lock:
                    self.api.SetVariable(
                        "tessedit_char_whitelist",
                        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,;:!?-_()[]{}<>@#$%^&*+=|\\~`\"'",
                    )

            if not multi_crop:
                with self.api_lock:
                    self.api.SetRectangle(
                        rect.x(), rect.y(), rect.width(), rect.height()
                    )

            text = ""
            extras = {}
            with self.api_lock:
                text = self.api.GetUTF8Text().strip()
                if text != "":
                    # get the per-character boxes using an iterator with RIL_SYMBOL level
                    it = self.api.GetIterator()
                    extras["boxes"] = []
                    wh_ratios = []
                    for w in iterate_level(it, RIL.SYMBOL):
                        char = w.GetUTF8Text(RIL.SYMBOL)
                        box_tuple = w.BoundingBox(RIL.SYMBOL)
                        if (
                            box_tuple is None
                            or char is None
                            or char == ""
                            or len(box_tuple) != 4
                        ):
                            continue
                        box = {
                            "x": box_tuple[0],
                            "y": box_tuple[1],
                            "w": box_tuple[2] - box_tuple[0],
                            "h": box_tuple[3] - box_tuple[1],
                        }
                        # box is a dict with x, y, w and h
                        if scale_x != 1.0 or scale_y != 1.0:
                            box["x"] = int(box["x"] / scale_x)
                            box["y"] = int(box["y"] / scale_y)
                            box["w"] = int(box["w"] / scale_x)
                            box["h"] = int(box["h"] / scale_y)
                        if effectiveRect is not None:
                            box["x"] = int(box["x"] + effectiveRect.x())
                            box["y"] = int(box["y"] + effectiveRect.y())
                        extras["boxes"].append(box)
                        # if char is a "wide character" (like 0,2,3,4,5,6,7,8,9), add the width-to-height ratio
                        if char in "023456789":
                            wh_ratios.append(box["w"] / box["h"])
                    if (
                        "normalize_wh_ratio" in rect.settings
                        and rect.settings["normalize_wh_ratio"]
                        and "median_wh_ratio" not in rect.settings
                        and len(wh_ratios) > 0
                    ):
                        rect.settings["median_wh_ratio"] = np.median(wh_ratios)

            textstate = TextDetectionTargetWithResult.ResultState.Success
            if rect.settings is not None:
                if "format_regex" in rect.settings:
                    # validate the regex format is valid
                    if is_valid_regex(rect.settings["format_regex"]):
                        # check the text matches the regex fully
                        if not re.fullmatch(rect.settings["format_regex"], text):
                            textstate = (
                                TextDetectionTargetWithResult.ResultState.FailedFilter
                            )
                if "conf_thresh" in rect.settings:
                    with self.api_lock:
                        meanConf = self.api.MeanTextConf()
                    if meanConf < rect.settings["conf_thresh"]:
                        textstate = (
                            TextDetectionTargetWithResult.ResultState.FailedFilter
                        )
                if "smoothing" in rect.settings:
                    if rect.settings["smoothing"]:
                        # apply smoother
                        text = rect.ocrResultPerCharacterSmoother.get_smoothed_result(
                            text
                        )
                        if text is None:
                            text = ""
                if "remove_leading_zeros" in rect.settings:
                    if rect.settings["remove_leading_zeros"]:
                        # remove leading zeros
                        text = text.lstrip("0")
                        if text == "":
                            text = "0"
                if "ordinal_indicator" in rect.settings:
                    if rect.settings["ordinal_indicator"]:
                        # add ordinal indicator
                        text = add_ordinal_indicator(text)

            if text == "":
                textstate = TextDetectionTargetWithResult.ResultState.Empty

            texts.append(TextDetectionResult(text, textstate, effectiveRect, extras))
        return texts
