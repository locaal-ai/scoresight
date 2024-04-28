import enum
from PySide6.QtCore import QRectF


class OCRResultPerCharacterSmoother:
    # This class is used to smooth the OCR results per character.
    # It holds a list of the last n OCR results (string), split to characters.
    # it returns the most common character in the list as the smoothed result per each
    # position in the string.

    def __init__(self, max_history=5):
        self.max_history = max_history
        self.history = []

    def get_smoothed_result(self, result: str) -> str:
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        self.history.append(result)

        # split the results to characters
        characters = []
        for result in self.history:
            characters.append(list(result))
        # find the most common character in each position
        smoothed_result = ""
        for i in range(len(characters[0])):
            # get the i'th character from each result
            chars = []
            for result in characters:
                if len(result) > i:
                    chars.append(result[i])
            # find the most common character
            if len(chars) > 0:
                smoothed_result += max(set(chars), key=chars.count)
        return smoothed_result

    def clear(self):
        self.history.clear()


class TextDetectionTarget(QRectF):
    def __init__(self, x, y, width, height, name, settings: dict | None = None):
        super().__init__(x, y, width, height)
        self.name = name
        self.settings = settings
        self.ocrResultPerCharacterSmoother = OCRResultPerCharacterSmoother()
        self.last_image = None
        self.last_text = None


class TextDetectionTargetWithResult(TextDetectionTarget):
    class ResultState(enum.Enum):
        Success = 0
        FailedFilter = 1
        Empty = 2
        SameNoChange = 3

    def __init__(
        self,
        detection_target: TextDetectionTarget,
        result,
        result_state,
        effectiveRect=None,
        extras=None,
    ):
        super().__init__(
            detection_target.x(),
            detection_target.y(),
            detection_target.width(),
            detection_target.height(),
            detection_target.name,
            detection_target.settings,
        )
        self.result = result
        self.result_state = result_state
        self.effectiveRect = effectiveRect
        self.extras = extras

    def to_dict(self):
        return {
            "name": self.name,
            "text": self.result,
            "state": self.result_state.name,
            "rect": {
                "x": self.x(),
                "y": self.y(),
                "width": self.width(),
                "height": self.height(),
            },
        }
