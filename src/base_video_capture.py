import cv2


class BaseVideoCapture:
    def __init__(self, capture_id: int | str, capture_backend: int = cv2.CAP_ANY):
        self.capture_id = capture_id
        self.capture_backend = capture_backend

    def isOpened(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError

    def set(self, propId, value):
        raise NotImplementedError

    def get(self, propId):
        raise NotImplementedError
