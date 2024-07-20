import json
import os
from PySide6.QtCore import QObject, Signal
from platformdirs import user_data_dir
from defaults import info_for_box_name, normalize_settings_dict

from text_detection_target import TextDetectionTarget
from sc_logging import logger


data_subscribers = {}


def subscribe_to_data(file_path, document_name, callback):
    # Subscribe to data changes in a JSON file
    # prepend the user data directory
    file_path = os.path.join(user_data_dir("scoresight"), file_path)

    if file_path not in data_subscribers:
        data_subscribers[file_path] = {}
    if document_name not in data_subscribers[file_path]:
        data_subscribers[file_path][document_name] = []
    data_subscribers[file_path][document_name].append(callback)


def store_data(file_path, document_name, data):
    # Store data into a JSON file
    # get the user data directory
    data_dir = user_data_dir("scoresight")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # prepend the user data directory
    file_path = os.path.join(data_dir, file_path)

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                documents = json.load(f)
            except json.JSONDecodeError:
                documents = {}
    else:
        documents = {}

    documents[document_name] = data

    # notify subscribers
    if file_path in data_subscribers and document_name in data_subscribers[file_path]:
        for callback in data_subscribers[file_path][document_name]:
            callback(data)

    with open(file_path, "w") as f:
        json.dump(documents, f, indent=2)


def remove_data(file_path, document_name):
    # Remove data from a JSON file
    # prepend the user data directory
    file_path = os.path.join(user_data_dir("scoresight"), file_path)

    if not os.path.exists(file_path):
        return

    with open(file_path, "r") as f:
        documents = json.load(f)

    if document_name in documents:
        del documents[document_name]

    # notify subscribers
    if file_path in data_subscribers and document_name in data_subscribers[file_path]:
        for callback in data_subscribers[file_path][document_name]:
            callback(None)

    with open(file_path, "w") as f:
        json.dump(documents, f, indent=2)


def fetch_data(file_path, document_name, default=None):
    # Fetch data from a JSON file
    # prepend the user data directory
    file_path = os.path.join(user_data_dir("scoresight"), file_path)

    if not os.path.exists(file_path):
        return default

    with open(file_path, "r") as f:
        try:
            documents = json.load(f)
        except json.JSONDecodeError:
            return default

    if document_name in documents:
        return documents[document_name]
    else:
        return default


def store_custom_box_name(custom_box_name: str):
    # get the current custom box names
    custom_boxes_names = fetch_data("scoresight.json", "custom_boxes_names", [])
    if custom_box_name in custom_boxes_names:
        return
    custom_boxes_names.append(custom_box_name)
    # Store the custom box name in the scoresight.json file
    store_data("scoresight.json", "custom_boxes_names", custom_boxes_names)


def rename_custom_box_name_in_storage(old_name: str, new_name: str):
    # get the current custom box names
    custom_boxes_names = fetch_data("scoresight.json", "custom_boxes_names", [])
    if old_name in custom_boxes_names:
        custom_boxes_names.remove(old_name)
    custom_boxes_names.append(new_name)
    # Store the custom box name in the scoresight.json file
    store_data("scoresight.json", "custom_boxes_names", custom_boxes_names)


def remove_custom_box_name_in_storage(custom_box_name: str):
    # get the current custom box names
    custom_boxes_names = fetch_data("scoresight.json", "custom_boxes_names", [])
    if custom_box_name in custom_boxes_names:
        custom_boxes_names.remove(custom_box_name)
    # Store the custom box name in the scoresight.json file
    store_data("scoresight.json", "custom_boxes_names", custom_boxes_names)


def fetch_custom_box_names():
    return fetch_data("scoresight.json", "custom_boxes_names", [])


class TextDetectionTargetMemoryStorage(QObject):
    # This class is used to store the text detection targets in memory

    data_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self._data: list[TextDetectionTarget] = []

    def add_item(self, item: TextDetectionTarget):
        self._data.append(item)
        self.data_changed.emit(self._data)

    def remove_item(self, item_name: str):
        for i, item in enumerate(self._data):
            if item.name == item_name:
                del self._data[i]
                break
        self.data_changed.emit(self._data)

    def clear(self):
        self._data.clear()
        self.data_changed.emit(self._data)

    def edit_item(self, item_name: str, new_item: TextDetectionTarget):
        for i, item in enumerate(self._data):
            if item.name == item_name:
                self._data[i].setRect(
                    new_item.x(), new_item.y(), new_item.width(), new_item.height()
                )
                self._data[i].settings = new_item.settings
                self.data_changed.emit(self._data)
                return
        logger.warn("unable to find item to edit in storage: " + item_name)

    def rename_item(self, old_name: str, new_name: str):
        for i, item in enumerate(self._data):
            if item.name == old_name:
                self._data[i].name = new_name
                self.data_changed.emit(self._data)
                return True
        logger.warn("unable to find item to rename in storage: " + old_name)
        return False

    def get_data(self):
        return self._data

    def is_empty(self):
        return len(self._data) == 0

    def find_item_by_name(self, name: str):
        for item in self._data:
            if item.name == name:
                return item
        return None

    def loadBoxesFromStorage(self) -> bool:
        # load the boxes from scoresight.json
        boxes = fetch_data("scoresight.json", "boxes")
        if not boxes:
            return False
        return self.loadBoxesFromDict(boxes)

    def loadBoxesFromFile(self, file_path) -> bool:
        # load the boxes from a file
        with open(file_path, "r") as f:
            boxes = json.load(f)
        return self.loadBoxesFromDict(boxes)

    def loadBoxesFromDict(self, boxes) -> bool:
        data_backup = self._data.copy()
        self._data.clear()
        try:
            for box in boxes:
                box_info = info_for_box_name(box["name"])
                if "settings" not in box:
                    box["settings"] = {}
                # set the position of the box
                self._data.append(
                    TextDetectionTarget(
                        box["rect"]["x"],
                        box["rect"]["y"],
                        box["rect"]["width"],
                        box["rect"]["height"],
                        box["name"],
                        normalize_settings_dict(box["settings"], box_info),
                    )
                )
            logger.debug("loaded boxes")
            self.data_changed.emit(self._data)
        except Exception as e:
            logger.error("error loading boxes: " + str(e))
            self._data = data_backup
            return False
        return True

    def getBoxesForStorage(self):
        # save all the boxes to scoresight.json
        boxes = []
        for detectionTarget in self._data:
            detectionTarget.settings = normalize_settings_dict(
                detectionTarget.settings, info_for_box_name(detectionTarget.name)
            )
            boxes.append(
                {
                    "name": detectionTarget.name,
                    "rect": {
                        "x": detectionTarget.x(),
                        "y": detectionTarget.y(),
                        "width": detectionTarget.width(),
                        "height": detectionTarget.height(),
                    },
                    "settings": {
                        "obs_source_name": detectionTarget.settings.get(
                            "obs_source_name"
                        ),
                        "format_regex": detectionTarget.settings.get("format_regex"),
                        "smoothing": detectionTarget.settings.get("smoothing"),
                        "skip_empty": detectionTarget.settings.get("skip_empty"),
                        "conf_thresh": detectionTarget.settings.get("conf_thresh"),
                        "cleanup_thresh": detectionTarget.settings.get(
                            "cleanup_thresh"
                        ),
                        "dilate": detectionTarget.settings.get("dilate"),
                        "skew": detectionTarget.settings.get("skew"),
                        "vscale": detectionTarget.settings.get("vscale"),
                        "autocrop": detectionTarget.settings.get("autocrop"),
                        "skip_similar_image": detectionTarget.settings.get(
                            "skip_similar_image"
                        ),
                        "remove_leading_zeros": detectionTarget.settings.get(
                            "remove_leading_zeros"
                        ),
                        "rescale_patch": detectionTarget.settings.get("rescale_patch"),
                        "normalize_wh_ratio": detectionTarget.settings.get(
                            "normalize_wh_ratio"
                        ),
                        "invert_patch": detectionTarget.settings.get("invert_patch"),
                        "dot_detector": detectionTarget.settings.get("dot_detector"),
                        "ordinal_indicator": detectionTarget.settings.get(
                            "ordinal_indicator"
                        ),
                        "binarization_method": detectionTarget.settings.get(
                            "binarization_method"
                        ),
                    },
                }
            )
        return boxes

    def saveBoxesToFile(self, file_path):
        boxes = self.getBoxesForStorage()
        with open(file_path, "w") as f:
            json.dump(boxes, f, indent=2)

    def saveBoxesToStorage(self):
        boxes = self.getBoxesForStorage()
        store_data("scoresight.json", "boxes", boxes)
