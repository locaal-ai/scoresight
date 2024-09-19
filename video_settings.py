import cv2

from PySide6.QtWidgets import QDialog
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

    def init_ui(self, cap):
        self.cap = cap
        self.ui.buttonBox.accepted.connect(self.save_settings)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.spinBox_fps.setValue(int(cap.get(cv2.CAP_PROP_FPS)))
        self.ui.comboBox_resolution.setCurrentText(
            f"{cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}"
        )
        self.populate_supported_fourcc()

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
        store_data(
            "scoresight.json",
            "video_settings",
            {
                "fps": fps,
                "width": width,
                "height": height,
                "fourcc": fourcc,
            },
        )
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        if width > 0:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        if height > 0:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        fourcc_int = int.from_bytes(fourcc.encode(), "little")
        self.cap.set(cv2.CAP_PROP_FOURCC, fourcc_int)
        print(f"FPS: {fps}, Resolution: {width}x{height}, FourCC: {fourcc}")
        logger.info(f"FPS: {fps}, Resolution: {width}x{height}, FourCC: {fourcc}")
        print(
            f"FPS: {self.cap.get(cv2.CAP_PROP_FPS)}, Resolution: {self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}, FourCC: {fourcc_to_str(self.cap.get(cv2.CAP_PROP_FOURCC))}"
        )

        self.close()
