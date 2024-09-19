import cv2
import platform

from PySide6.QtWidgets import QDialog
from camera_thread import OpenCVVideoCaptureWithSettings
from sc_logging import logger
from ui_video_settings import Ui_Dialog as Ui_VideoSettingsDialog
from storage import store_data


def fourcc_to_str(fourcc):
    if fourcc == 0:
        return "NULL"
    if type(fourcc) == str:
        return fourcc
    if type(fourcc) == bytes:
        return fourcc.decode()
    if type(fourcc) != int:
        fourcc = int(fourcc)
    return "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])


def get_supported_fourcc(cap):
    fourcc_list = [
        cv2.VideoWriter_fourcc(*"MJPG"),
        cv2.VideoWriter_fourcc(*"YUYV"),
        cv2.VideoWriter_fourcc(*"YUY2"),
        cv2.VideoWriter_fourcc(*"YU12"),
        cv2.VideoWriter_fourcc(*"YV12"),
        cv2.VideoWriter_fourcc(*"RGB3"),
        cv2.VideoWriter_fourcc(*"H264"),
        cv2.VideoWriter_fourcc(*"X264"),
        cv2.VideoWriter_fourcc(*"XVID"),
        cv2.VideoWriter_fourcc(*"MPEG"),
        cv2.VideoWriter_fourcc(*"NV12"),
        cv2.VideoWriter_fourcc(*"I420"),
    ]

    original_fourcc = int(cap.get(cv2.CAP_PROP_FOURCC)) & 0xFFFFFFFF
    supported_fourccs = [fourcc_to_str(original_fourcc)]

    for fourcc in fourcc_list:
        cap.set(cv2.CAP_PROP_FOURCC, fourcc)
        actual_fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        if actual_fourcc == fourcc:
            fourcc_str = fourcc_to_str(fourcc)
            if fourcc_str not in supported_fourccs:
                supported_fourccs.append(fourcc_str)

    cap.set(cv2.CAP_PROP_FOURCC, original_fourcc)

    return supported_fourccs


class VideoSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VideoSettingsDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.save_settings)
        self.ui.buttonBox.rejected.connect(self.close)

    def init_ui(self, cap: OpenCVVideoCaptureWithSettings):
        self.cap = cap
        self.ui.spinBox_fps.setValue(int(self.cap.get(cv2.CAP_PROP_FPS)))
        self.ui.comboBox_resolution.setCurrentText(
            f"{self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}"
        )
        self.populate_supported_fourcc()
        self.populate_video_props()
        self.populate_backend_combo()

    def populate_backend_combo(self):
        self.ui.comboBox_captureBackend.clear()
        self.ui.comboBox_captureBackend.addItem("Auto", cv2.CAP_ANY)
        if platform.system() == "Windows":
            self.ui.comboBox_captureBackend.addItem("DShow", cv2.CAP_DSHOW)
            self.ui.comboBox_captureBackend.addItem(
                "Microsoft Media Foundation", cv2.CAP_MSMF
            )
            self.ui.comboBox_captureBackend.addItem(
                "Microsoft Windows Runtime", cv2.CAP_WINRT
            )
        elif platform.system() == "Linux":
            self.ui.comboBox_captureBackend.addItem("V4L", cv2.CAP_V4L)
            self.ui.comboBox_captureBackend.addItem("GStreamer", cv2.CAP_GSTREAMER)
        elif platform.system() == "Darwin":
            self.ui.comboBox_captureBackend.addItem(
                "AVFoundation", cv2.CAP_AVFOUNDATION
            )
        self.ui.comboBox_captureBackend.setCurrentIndex(
            self.ui.comboBox_captureBackend.findData(self.cap.get(cv2.CAP_PROP_BACKEND))
        )

    def populate_video_props(self):
        # scan all opencv properties and write to plainTextEdit_videoProps
        video_props = [
            (cv2.CAP_PROP_POS_MSEC, "CAP_PROP_POS_MSEC"),
            (cv2.CAP_PROP_POS_FRAMES, "CAP_PROP_POS_FRAMES"),
            (cv2.CAP_PROP_POS_AVI_RATIO, "CAP_PROP_POS_AVI_RATIO"),
            (cv2.CAP_PROP_FRAME_WIDTH, "CAP_PROP_FRAME_WIDTH"),
            (cv2.CAP_PROP_FRAME_HEIGHT, "CAP_PROP_FRAME_HEIGHT"),
            (cv2.CAP_PROP_FPS, "CAP_PROP_FPS"),
            (cv2.CAP_PROP_FOURCC, "CAP_PROP_FOURCC"),
            (cv2.CAP_PROP_FRAME_COUNT, "CAP_PROP_FRAME_COUNT"),
            (cv2.CAP_PROP_FORMAT, "CAP_PROP_FORMAT"),
            (cv2.CAP_PROP_MODE, "CAP_PROP_MODE"),
            (cv2.CAP_PROP_BRIGHTNESS, "CAP_PROP_BRIGHTNESS"),
            (cv2.CAP_PROP_CONTRAST, "CAP_PROP_CONTRAST"),
            (cv2.CAP_PROP_SATURATION, "CAP_PROP_SATURATION"),
            (cv2.CAP_PROP_HUE, "CAP_PROP_HUE"),
            (cv2.CAP_PROP_GAIN, "CAP_PROP_GAIN"),
            (cv2.CAP_PROP_EXPOSURE, "CAP_PROP_EXPOSURE"),
            (cv2.CAP_PROP_CONVERT_RGB, "CAP_PROP_CONVERT_RGB"),
            (cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, "CAP_PROP_WHITE_BALANCE_BLUE_U"),
            (cv2.CAP_PROP_RECTIFICATION, "CAP_PROP_RECTIFICATION"),
            (cv2.CAP_PROP_MONOCHROME, "CAP_PROP_MONOCHROME"),
            (cv2.CAP_PROP_SHARPNESS, "CAP_PROP_SHARPNESS"),
            (cv2.CAP_PROP_AUTO_EXPOSURE, "CAP_PROP_AUTO_EXPOSURE"),
            (cv2.CAP_PROP_GAMMA, "CAP_PROP_GAMMA"),
            (cv2.CAP_PROP_TEMPERATURE, "CAP_PROP_TEMPERATURE"),
            (cv2.CAP_PROP_TRIGGER, "CAP_PROP_TRIGGER"),
            (cv2.CAP_PROP_TRIGGER_DELAY, "CAP_PROP_TRIGGER_DELAY"),
            (cv2.CAP_PROP_WHITE_BALANCE_RED_V, "CAP_PROP_WHITE_BALANCE_RED_V"),
            (cv2.CAP_PROP_ZOOM, "CAP_PROP_ZOOM"),
            (cv2.CAP_PROP_FOCUS, "CAP_PROP_FOCUS"),
            (cv2.CAP_PROP_GUID, "CAP_PROP_GUID"),
            (cv2.CAP_PROP_ISO_SPEED, "CAP_PROP_ISO_SPEED"),
            (cv2.CAP_PROP_BACKLIGHT, "CAP_PROP_BACKLIGHT"),
            (cv2.CAP_PROP_PAN, "CAP_PROP_PAN"),
            (cv2.CAP_PROP_TILT, "CAP_PROP_TILT"),
            (cv2.CAP_PROP_ROLL, "CAP_PROP_ROLL"),
            (cv2.CAP_PROP_IRIS, "CAP_PROP_IRIS"),
            (cv2.CAP_PROP_SETTINGS, "CAP_PROP_SETTINGS"),
            (cv2.CAP_PROP_BUFFERSIZE, "CAP_PROP_BUFFERSIZE"),
            (cv2.CAP_PROP_AUTOFOCUS, "CAP_PROP_AUTOFOCUS"),
            (cv2.CAP_PROP_SAR_NUM, "CAP_PROP_SAR_NUM"),
            (cv2.CAP_PROP_SAR_DEN, "CAP_PROP_SAR_DEN"),
            (cv2.CAP_PROP_BACKEND, "CAP_PROP_BACKEND"),
            (cv2.CAP_PROP_CHANNEL, "CAP_PROP_CHANNEL"),
            (cv2.CAP_PROP_AUTO_WB, "CAP_PROP_AUTO_WB"),
            (cv2.CAP_PROP_WB_TEMPERATURE, "CAP_PROP_WB_TEMPERATURE"),
            (cv2.CAP_PROP_CODEC_PIXEL_FORMAT, "CAP_PROP_CODEC_PIXEL_FORMAT"),
            (cv2.CAP_PROP_BITRATE, "CAP_PROP_BITRATE"),
            (cv2.CAP_PROP_ORIENTATION_META, "CAP_PROP_ORIENTATION_META"),
            (cv2.CAP_PROP_ORIENTATION_AUTO, "CAP_PROP_ORIENTATION_AUTO"),
            (cv2.CAP_PROP_HW_ACCELERATION, "CAP_PROP_HW_ACCELERATION"),
            (cv2.CAP_PROP_HW_DEVICE, "CAP_PROP_HW_DEVICE"),
            (
                cv2.CAP_PROP_HW_ACCELERATION_USE_OPENCL,
                "CAP_PROP_HW_ACCELERATION_USE_OPENCL",
            ),
            (cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, "CAP_PROP_OPEN_TIMEOUT_MSEC"),
            (cv2.CAP_PROP_READ_TIMEOUT_MSEC, "CAP_PROP_READ_TIMEOUT_MSEC"),
            (cv2.CAP_PROP_STREAM_OPEN_TIME_USEC, "CAP_PROP_STREAM_OPEN_TIME_USEC"),
            (cv2.CAP_PROP_VIDEO_TOTAL_CHANNELS, "CAP_PROP_VIDEO_TOTAL_CHANNELS"),
            (cv2.CAP_PROP_VIDEO_STREAM, "CAP_PROP_VIDEO_STREAM"),
            (cv2.CAP_PROP_AUDIO_STREAM, "CAP_PROP_AUDIO_STREAM"),
            (cv2.CAP_PROP_AUDIO_POS, "CAP_PROP_AUDIO_POS"),
            (cv2.CAP_PROP_AUDIO_SHIFT_NSEC, "CAP_PROP_AUDIO_SHIFT_NSEC"),
            (cv2.CAP_PROP_AUDIO_DATA_DEPTH, "CAP_PROP_AUDIO_DATA_DEPTH"),
            (
                cv2.CAP_PROP_AUDIO_SAMPLES_PER_SECOND,
                "CAP_PROP_AUDIO_SAMPLES_PER_SECOND",
            ),
            (cv2.CAP_PROP_AUDIO_BASE_INDEX, "CAP_PROP_AUDIO_BASE_INDEX"),
            (cv2.CAP_PROP_AUDIO_TOTAL_CHANNELS, "CAP_PROP_AUDIO_TOTAL_CHANNELS"),
            (cv2.CAP_PROP_AUDIO_TOTAL_STREAMS, "CAP_PROP_AUDIO_TOTAL_STREAMS"),
            (cv2.CAP_PROP_AUDIO_SYNCHRONIZE, "CAP_PROP_AUDIO_SYNCHRONIZE"),
            (cv2.CAP_PROP_LRF_HAS_KEY_FRAME, "CAP_PROP_LRF_HAS_KEY_FRAME"),
            (cv2.CAP_PROP_CODEC_EXTRADATA_INDEX, "CAP_PROP_CODEC_EXTRADATA_INDEX"),
            (cv2.CAP_PROP_FRAME_TYPE, "CAP_PROP_FRAME_TYPE"),
            (cv2.CAP_PROP_N_THREADS, "CAP_PROP_N_THREADS"),
        ]
        video_props_str = [
            f"{prop[1]}: {self.cap.get(prop[0])}" for prop in video_props
        ]
        self.ui.plainTextEdit_videoProps.setPlainText("\n".join(video_props_str))

    def populate_supported_fourcc(self):
        supported_fourccs = get_supported_fourcc(self.cap)
        self.ui.comboBox_fourcc.clear()
        self.ui.comboBox_fourcc.addItems(supported_fourccs)

    def save_settings(self):
        fps = self.ui.spinBox_fps.value()
        resolution = self.ui.comboBox_resolution.currentText()
        if "x" in resolution:
            resolution = resolution.split("x")
            width = int(resolution[0])
            height = int(resolution[1])
        else:
            width = -1
            height = -1
        fourcc = self.ui.comboBox_fourcc.currentText()
        store_data("scoresight.json", "fps", fps)
        store_data("scoresight.json", "width", width)
        store_data("scoresight.json", "height", height)
        store_data("scoresight.json", "fourcc", fourcc)
        store_data(
            "scoresight.json", "backend", self.ui.comboBox_captureBackend.currentData()
        )

        self.close()
