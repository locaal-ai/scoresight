class FieldType:
    # Enum for the type of the field
    NUMBER = 0
    TIME = 1
    TEXT = 2


# 0 - Time MM:ss and ss.m
# 1 - Time MM:ss
# 2 - Time ss.m
# 3 - Time 00-59
# 4 - Shotclock 00-39
# 5 - Score 1dd
# 6 - Score ddd
# 7 - Period 1-4
# 8 - Period d
# 9 - Alphanumeric
# 10 - Any text
# 11 - Any number
# 12 - Custom
format_prefixes = [
    "^(?:(?:[0-5]?\\d:[0-5]\\d)|(?:[0-5]?\\d\\.\\d))$",  # Time MM:ss and ss.m
    "^[0-5]?\\d:[0-5]\\d$",  # Time MM:ss
    "^[0-5]?\\d\\.\\d$",  # Time ss.m
    "^[0-5]\\d$",  # Time 00-59
    "^[0-3]\\d$",  # Shotclock 00-39
    "^1?\\d{1,2}$",  # Score 1dd
    "^\\d{1,3}$",  # Score ddd
    "^[1-4]{1}$",  # Period 1-4
    "^\\d{1}$",  # Period d
    "^[A-Za-z0-9]*$",  # Alphanumeric
    "^.*$",  # Any text
    "^\\d*$",  # Any number
    "^.*$",  # Custom
]


# Default values for the scoreboard
default_boxes = [
    {
        "name": "Home Score",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 120,
        "height": 100,
        "obs_source_name": "Home score",
        "format_regex": format_prefixes[5],
        "ordinal_indicator": False,
    },
    {
        "name": "Away Score",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 120,
        "height": 100,
        "obs_source_name": "Away score",
        "format_regex": format_prefixes[5],
        "ordinal_indicator": False,
    },
    {
        "name": "Time",
        "type": FieldType.TIME,
        "x": 0,
        "y": 0,
        "width": 170,
        "height": 100,
        "obs_source_name": "Clock",
        "format_regex": format_prefixes[0],
        "ordinal_indicator": False,
    },
    {
        "name": "Period",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 50,
        "height": 80,
        "obs_source_name": "Period",
        "format_regex": format_prefixes[7],
        "ordinal_indicator": True,
    },
    {
        "name": "Home Fouls",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 80,
        "height": 80,
        "obs_source_name": "#Home Fouls",
        "format_regex": format_prefixes[11],
        "ordinal_indicator": False,
    },
    {
        "name": "Away Fouls",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 80,
        "height": 80,
        "obs_source_name": "#Away Fouls",
        "format_regex": format_prefixes[11],
        "ordinal_indicator": False,
    },
    {
        "name": "Shot Clock",
        "type": FieldType.NUMBER,
        "x": 0,
        "y": 0,
        "width": 150,
        "height": 100,
        "obs_source_name": "shotclock",
        "format_regex": format_prefixes[4],
        "ordinal_indicator": False,
    },
]
default_custom_box_info = {
    "type": FieldType.NUMBER,
    "x": 0,
    "y": 0,
    "width": 150,
    "height": 100,
    "obs_source_name": "",
    "format_regex": format_prefixes[11],
    "ordinal_indicator": False,
}


def info_for_box_name(name):
    # Get the info for a box name
    for box in default_boxes:
        if box["name"] == name:
            return box
    return default_custom_box_info


def normalize_settings_dict(settings, box_info):
    # Normalize the settings dict with default values if they are not present
    if not settings:
        settings = {}
    if not box_info:
        box_info = {
            "obs_source_name": "",
            "format_regex": format_prefixes[11],
            "type": FieldType.NUMBER,
            "ordinal_indicator": False,
        }
    return {
        "obs_source_name": (
            settings["obs_source_name"]
            if "obs_source_name" in settings
            else box_info["obs_source_name"]
        ),
        "format_regex": (
            settings["format_regex"]
            if "format_regex" in settings
            else box_info["format_regex"]
        ),
        "type": (settings["type"] if "type" in settings else box_info["type"]),
        "smoothing": (settings["smoothing"] if "smoothing" in settings else False),
        "skip_empty": (settings["skip_empty"] if "skip_empty" in settings else True),
        "conf_thresh": (settings["conf_thresh"] if "conf_thresh" in settings else 0.5),
        "cleanup_thresh": (
            settings["cleanup_thresh"] if "cleanup_thresh" in settings else 0
        ),
        "dilate": (settings["dilate"] if "dilate" in settings else 1),
        "skew": (settings["skew"] if "skew" in settings else 0),
        "vscale": (settings["vscale"] if "vscale" in settings else 10),
        "autocrop": (settings["autocrop"] if "autocrop" in settings else False),
        "skip_similar_image": (
            settings["skip_similar_image"]
            if "skip_similar_image" in settings
            else False
        ),
        "remove_leading_zeros": (
            settings["remove_leading_zeros"]
            if "remove_leading_zeros" in settings
            else False
        ),
        "rescale_patch": (
            settings["rescale_patch"] if "rescale_patch" in settings else True
        ),
        "normalize_wh_ratio": (
            settings["normalize_wh_ratio"]
            if "normalize_wh_ratio" in settings
            else False
        ),
        "invert_patch": (
            settings["invert_patch"] if "invert_patch" in settings else False
        ),
        "dot_detector": (
            settings["dot_detector"] if "dot_detector" in settings else False
        ),
        "binarization_method": (
            settings["binarization_method"] if "binarization_method" in settings else 0
        ),
        "ordinal_indicator": (
            settings["ordinal_indicator"]
            if "ordinal_indicator" in settings
            else box_info["ordinal_indicator"]
        ),
    }
