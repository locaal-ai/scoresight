from setuptools import setup, Extension
import pybind11

setup(
    name="win32DeviceEnumBind",
    version="0.0.1",
    ext_modules=[
        Extension(
            "win32DeviceEnumBind",
            ["video_devices_enumerator_ds.cpp"],
            include_dirs=[pybind11.get_include()],
            language="c++",
            libraries=["strmiids", "ole32", "oleaut32", "uuid", "quartz"],
        ),
    ],
    setup_requires=["pybind11"],
)
