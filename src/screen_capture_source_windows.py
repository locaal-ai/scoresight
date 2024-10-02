import cv2
import numpy as np
import pygetwindow as gw
import numpy as np
import win32gui
import win32ui
import win32con
import win32api
from sc_logging import logger
from ctypes import windll


class ScreenCaptureWindows:
    @staticmethod
    def list_windows():
        # list the windows on the screen
        windows = gw.getAllTitles()
        return [(w, w) for w in windows if w != ""]

    def __init__(self, window_name):
        self.capture_whole_screen = (
            window_name is None
            or window_name == ""
            or (type(window_name) == int and window_name < 0)
        )

        self.hwnd = 0
        if self.capture_whole_screen:
            # Get the device context (DC) for the entire screen
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            # Find the window
            self.hwnd = win32gui.FindWindow(None, window_name)

        if self.hwnd == 0:
            logger.error("No window found")
            return

        # Get the window device context (DC)
        self.hwndDC = win32gui.GetWindowDC(self.hwnd)
        if self.hwndDC == 0:
            logger.error("Error getting window device context for window")
            return
        # Create a memory device context
        self.mfcDC = win32ui.CreateDCFromHandle(self.hwndDC)
        if self.mfcDC is None:
            logger.error("Error creating memory device context for window")
            return
        self.saveDC = self.mfcDC.CreateCompatibleDC()
        if self.saveDC is None:
            logger.error(f"Error creating compatible memory device context for window")
            return

    def isOpened(self):
        return self.hwnd != 0

    def release(self):
        try:
            self.saveDC.DeleteDC()
            self.mfcDC.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, self.hwndDC)
        except:
            logger.exception("Error releasing screen capture resources")

    def read(self):
        if self.hwnd == 0:
            return False, None

        # check window handle is valid
        if not win32gui.IsWindow(self.hwnd):
            logger.error(f"Window handle {self.hwnd} is invalid")
            return False, None

        if not self.capture_whole_screen:
            # Get window dimensions
            left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
            width = right - left
            height = bot - top
        else:
            # Get the device context (DC) for the entire screen
            width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        # Create a bitmap object
        saveBitMap = win32ui.CreateBitmap()
        if saveBitMap is None:
            logger.error(f"Error creating bitmap for window")
            return False, None

        saveBitMap.CreateCompatibleBitmap(self.mfcDC, width, height)
        self.saveDC.SelectObject(saveBitMap)

        if self.capture_whole_screen:
            # use bitblt to copy the window image to the bitmap
            self.saveDC.BitBlt(
                (0, 0), (width, height), self.mfcDC, (left, top), win32con.SRCCOPY
            )
        else:
            # use print window to copy the window image to the bitmap
            result = windll.user32.PrintWindow(self.hwnd, self.saveDC.GetSafeHdc(), 3)
            if not result:
                logger.error(f"Unable to acquire screenshot! Result: {result}")
                return False, None

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape(
            (bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4)
        )

        win32gui.DeleteObject(saveBitMap.GetHandle())

        image = np.ascontiguousarray(img)  # Ensure array is contiguous
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        return True, image

    def get(self, prop) -> float:
        if self.hwnd == 0:
            return 0.0

        if prop == cv2.CAP_PROP_FRAME_WIDTH:
            return win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        elif prop == cv2.CAP_PROP_FRAME_HEIGHT:
            return win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        else:
            return 0.0
