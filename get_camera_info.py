import platform
from camera_info import CameraInfo
from ndi import NDICapture
from sc_logging import logger

# This file contains the code to get the camera information for the current OS


def get_camera_info_windows():
    from win32DeviceEnum import enum_devices_dshow

    device_info = []
    cameras = enum_devices_dshow.enumerate_video_devices_dshow()
    for camera in cameras:
        device_info.append(
            CameraInfo(
                camera[1], str(camera[0]), camera[0], CameraInfo.CameraType.OPENCV
            )
        )

    return device_info


def get_camera_info_mac():
    import AVFoundation as AV

    device_info = []
    devices = AV.AVCaptureDevice.devicesWithMediaType_(AV.AVMediaTypeVideo)

    for i, device in enumerate(devices):
        device_info.append(
            CameraInfo(
                device.localizedName(),
                device.uniqueID(),
                i,
                CameraInfo.CameraType.OPENCV,
            )
        )

    # sort by the ID, since opencv sorts by ID
    device_info.sort(key=lambda x: x.uuid)
    # update the ID
    for i, camera in enumerate(device_info):
        camera.id = i

    return device_info


def get_camera_info_linux():
    # Basic method using /dev/video* enumeration
    device_info = [
        CameraInfo(f"Camera {i}", f"/dev/{dev}", i, CameraInfo.CameraType.OPENCV)
        for i, dev in enumerate(device_info)
    ]
    return device_info


def get_camera_info() -> list[CameraInfo]:
    logger.info("Getting cameras info")
    os_name = platform.system()
    cameras = []
    if os_name == "Windows":
        cameras += get_camera_info_windows()
    elif os_name == "Darwin":
        cameras += get_camera_info_mac()
    elif os_name == "Linux":
        cameras += get_camera_info_linux()

    # Add NDI cameras
    cameras += NDICapture.get_camera_info_ndi()

    return cameras
