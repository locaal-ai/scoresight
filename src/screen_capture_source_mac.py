import Quartz
import objc
from Quartz.CoreGraphics import (
    CGImageGetWidth,
    CGImageGetHeight,
    CGImageGetDataProvider,
    CGDataProviderCopyData,
    CGWindowListCreateImage,
    CGRectInfinite,
    CGRectNull,
)
import numpy as np
from sc_logging import logger
import cv2


class ScreenCaptureMacOS:
    @staticmethod
    def list_windows():
        window_list = Quartz.CGWindowListCopyWindowInfo(
            Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
        )
        windows = []
        for window in window_list:
            # check if the window is an application window that has a layer of 0
            if window.get(Quartz.kCGWindowLayer) != 0:
                continue
            # Check if the window has a size and is not a menubar item
            if (
                window.get(Quartz.kCGWindowBounds).get("Width") > 0
                and window.get(Quartz.kCGWindowBounds).get("Height") > 0
            ):
                windows.append(
                    (
                        window.get(Quartz.kCGWindowOwnerName, ""),
                        window[Quartz.kCGWindowNumber],
                    )
                )
        return windows

    def __init__(self, windowId=None):
        self.windowId = windowId
        self.window = None
        self.width = 0
        self.height = 0
        if self.windowId is not None and self.windowId >= 0:
            # Capture a specific window by ID
            window_list = Quartz.CGWindowListCopyWindowInfo(
                Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
            )
            capture_window = [
                w for w in window_list if w[Quartz.kCGWindowNumber] == self.windowId
            ]
            if not capture_window:
                raise ValueError(f"No window with ID {self.windowId} found")
            self.window = capture_window[0]

    def isOpened(self):
        return self.window is not None

    def read(self):
        if self.windowId is None or self.windowId < 0:
            # Capture the entire screen
            cgimage = CGWindowListCreateImage(
                CGRectInfinite,
                Quartz.kCGWindowListOptionOnScreenOnly,
                Quartz.kCGNullWindowID,
                Quartz.kCGWindowImageDefault,
            )
        else:
            cgimage = CGWindowListCreateImage(
                CGRectNull,
                Quartz.kCGWindowListOptionIncludingWindow,
                self.windowId,
                Quartz.kCGWindowImageBoundsIgnoreFraming,
            )

        if cgimage is None:
            logger.warn(f"Failed to create image from window {self.windowId}")
            return False, None

        self.width = CGImageGetWidth(cgimage)
        self.height = CGImageGetHeight(cgimage)
        if self.width == 0 or self.height == 0:
            logger.warn(f"Invalid image size: {self.width}x{self.height}")
            return False, None

        data_provider = CGImageGetDataProvider(cgimage)
        data = CGDataProviderCopyData(data_provider)
        np_data = np.frombuffer(data, dtype=np.uint8)
        # calculate the width from the buffer size
        self.width = len(np_data) // self.height // 4
        image = np_data.reshape(
            (self.height, self.width, 4)
        )  # Assuming 4 channels (RGBA)
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        return True, image  # Convert to RGB

    def release(self):
        pass

    def get(self, prop) -> float:
        if prop == cv2.CAP_PROP_FRAME_WIDTH:
            return self.width
        elif prop == cv2.CAP_PROP_FRAME_HEIGHT:
            return self.height
        else:
            return 0.0
