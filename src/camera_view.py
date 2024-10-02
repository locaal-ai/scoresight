from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QPainter
from PySide6.QtCore import Signal

import numpy as np
import cv2

from camera_info import CameraInfo
from storage import TextDetectionTargetMemoryStorage, subscribe_to_data
from sc_logging import logger
from camera_thread import TimerThread


class CameraView(QGraphicsView):
    first_frame_received_signal = Signal()

    def __init__(
        self,
        camera_index: CameraInfo,
        detectionTargetsStorage: TextDetectionTargetMemoryStorage | None = None,
    ):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.timerThread = TimerThread(camera_index, detectionTargetsStorage)
        self.timerThread.update_signal.connect(self.update_pixmap)
        self.timerThread.update_error.connect(self.error_event)
        self.timerThread.start()
        self.scenePixmapItem = None
        self.detectionTargetsStorage = detectionTargetsStorage
        self.firstFrameReceived = False
        self.fps_text = None
        self.error_text = None
        self.showOSD = True
        self.camera_width = 0
        self.camera_height = 0
        subscribe_to_data("scoresight.json", "video_settings", self.resetFrame)

    def resetFrame(self, data):
        self.firstFrameReceived = False

    def getCameraCapture(self):
        return self.timerThread.video_capture

    def getCameraInfo(self):
        return self.timerThread.camera_info

    def setUpdateOnChange(self, updateOnChange):
        self.timerThread.updateOnChange = updateOnChange

    def toggleOSD(self, state):
        self.showOSD = state
        if self.fps_text is not None:
            self.fps_text.setVisible(state)

    def update_pixmap(self, frame):
        if self.timerThread is None:
            return

        # check if frame is not contiguous
        if not frame.flags["C_CONTIGUOUS"]:
            frame = np.ascontiguousarray(frame)

        # Create a QImage from the frame data
        image = QImage(
            frame.data,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            (
                QImage.Format.Format_Grayscale8
                if frame.ndim == 2
                else (
                    QImage.Format.Format_BGR888
                    if frame.shape[2] == 3
                    else QImage.Format.Format_RGBA8888
                )
            ),
        )

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(image)

        if self.scenePixmapItem is None:
            self.scenePixmapItem = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(self.scenePixmapItem)
            self.scenePixmapItem.setZValue(0)
            self.fitInView(self.scenePixmapItem, Qt.AspectRatioMode.KeepAspectRatio)
        else:
            refit = False
            # check if the pixmap is the same size as the current one
            if self.scenePixmapItem.pixmap().size() != pixmap.size():
                logger.info(f"scene size: {self.scene.sceneRect()}")
                refit = True
            self.scenePixmapItem.setPixmap(pixmap)
            if refit:
                self.scene.setSceneRect(0, 0, pixmap.width(), pixmap.height())
                logger.info(f"scene size: {self.scene.sceneRect()}")
                logger.info(f"Refitting view to new pixmap size: {pixmap.size()}")
                self.fitInView(self.scenePixmapItem, Qt.AspectRatioMode.KeepAspectRatio)
                self.centerOn(self.scenePixmapItem)

        if not self.firstFrameReceived:
            self.firstFrameReceived = True
            self.camera_width = self.timerThread.video_capture.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
            self.camera_height = self.timerThread.video_capture.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
            self.first_frame_received_signal.emit()

        # update the fps text
        fps_text = f"Frames/s: {self.timerThread.fps:.2f}\nUpdates/s: {self.timerThread.ups:.2f}\nPreviews/s: {self.timerThread.pps:.2f}\nResolution: {int(self.camera_width)}x{int(self.camera_height)}"
        if self.fps_text is None:
            self.fps_text = self.scene.addText(fps_text)
            self.fps_text.setPos(0, 0)
            self.fps_text.setZValue(2)
            self.fps_text.setDefaultTextColor(Qt.GlobalColor.white)
        else:
            self.fps_text.setPlainText(fps_text)
        # scale the text according to the view size so its always the same size
        self.fps_text.setScale(0.0015 * self.scenePixmapItem.boundingRect().width())

    def error_event(self, error):
        if self.error_text is not None:
            self.scene.removeItem(self.error_text)
        if error is not None:
            logger.error("Error: %s", error)
            # add the error to the scene
            self.error_text = self.scene.addText(f"⚠️ {error}")
            self.error_text.setDefaultTextColor(Qt.GlobalColor.red)
            self.error_text.setScale(0.004 * self.width())
            # diplay error on the bottom of the video view
            self.error_text.setPos(
                0, self.height() - self.error_text.boundingRect().height() - 10
            )

    def setFourCornersForHomography(self, corners: list[tuple[int]]):
        if corners is None or len(corners) != 4:
            if self.timerThread is not None:
                self.timerThread.homography = None
            return
        corners_as_array = np.array(corners, dtype=np.float32)
        # Calculate bounding rectangle
        x, y, w, h = cv2.boundingRect(corners_as_array)
        # Destination points (corners of the bounding rectangle)
        dst_points = np.array(
            [[x, y], [x + w, y], [x + w, y + h], [x, y + h]], dtype=np.float32
        )
        # calculate the homography from the corners to the rect
        self.timerThread.homography, _ = cv2.findHomography(
            corners_as_array, dst_points
        )

    def closeEvent(self, event):
        logger.debug("Close")
        if self.timerThread is not None:
            # Stop the timer thread
            self.timerThread.should_stop = True
            self.timerThread.wait()
            self.timerThread = None

        # Call the base class closeEvent method
        super().closeEvent(event)

    # on destroy, stop the timer
    def __del__(self):
        if self.timerThread is not None:
            self.timerThread.should_stop = True
            self.timerThread.wait()
            self.timerThread = None
