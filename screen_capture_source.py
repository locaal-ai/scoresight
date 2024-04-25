import platform


class ScreenCaptureNotImplemented:
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


# This is a simple example of how to use the screen capture source in the
# platform-independent part of the code.
if platform.system() == "Darwin":
    from screen_capture_source_mac import ScreenCaptureMacOS
    ScreenCapture = ScreenCaptureMacOS
elif platform.system() == "Windows":
    from screen_capture_source_windows import ScreenCaptureWindows
    ScreenCapture = ScreenCaptureWindows
else:
    ScreenCapture = ScreenCaptureNotImplemented
