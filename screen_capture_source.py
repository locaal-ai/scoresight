import platform
from typing import Union, Type


# Define a base class or protocol for screen capture
class ScreenCaptureBase:
    @staticmethod
    def list_windows():
        raise NotImplementedError

    def __init__(self, window_name):
        raise NotImplementedError

    def isOpened(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def get(self, prop) -> float:
        raise NotImplementedError


class ScreenCaptureDummy:
    @staticmethod
    def list_windows():
        return []

    def __init__(self, window_name):
        pass

    def isOpened(self):
        return False

    def release(self):
        pass

    def read(self):
        return False, None

    def get(self, prop) -> float:
        return 0.0


# This is a simple example of how to use the screen capture source in the
# platform-independent part of the code.
if platform.system() == "Darwin":
    from screen_capture_source_mac import ScreenCaptureMacOS as ScreenCapture
elif platform.system() == "Windows":
    from screen_capture_source_windows import ScreenCaptureWindows as ScreenCapture
else:
    ScreenCapture = ScreenCaptureDummy

ScreenCaptureType = Union[Type[ScreenCapture], Type[ScreenCaptureBase]]
