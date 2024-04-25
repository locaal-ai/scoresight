import sys
from os import path


def enumerate_video_devices_dshow() -> list[tuple[int, str]]:
    sys.path.append(path.abspath(path.dirname(__file__)))
    import win32DeviceEnumBind

    # Initialize COM
    win32DeviceEnumBind.InitializeCOM()

    # Call the enumeration function
    deviceArray = win32DeviceEnumBind.EnumerateVideoDevicesDShow()

    # Convert the array to a list of tuples
    devices = list(enumerate(deviceArray))

    # Uninitialize COM
    win32DeviceEnumBind.UninitializeCOM()

    return devices
