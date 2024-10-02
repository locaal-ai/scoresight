#include <windows.h>
#include <dshow.h>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

HRESULT InitializeCOM() {
    return CoInitialize(nullptr);
}

void UninitializeCOM() {
    CoUninitialize();
}

int EnumerateVideoDevicesDShow(std::vector<std::wstring>& deviceNames) {
    ICreateDevEnum *pDevEnum = nullptr;
    IEnumMoniker *pEnum = nullptr;
    deviceNames.clear();

    HRESULT hr = CoCreateInstance(CLSID_SystemDeviceEnum, nullptr, CLSCTX_INPROC, IID_ICreateDevEnum,
        reinterpret_cast<void**>(&pDevEnum));

    if (FAILED(hr)) {
        return -1;
    }

    hr = pDevEnum->CreateClassEnumerator(CLSID_VideoInputDeviceCategory, &pEnum, 0);
    if (!pEnum) {
        return -1;
    }

    IMoniker *pMoniker = nullptr;
    ULONG i_fetched;
    while (pEnum->Next(1, &pMoniker, &i_fetched) == S_OK) {
        IPropertyBag *pPropBag;
        hr = pMoniker->BindToStorage(0, 0, IID_PPV_ARGS(&pPropBag));
        if (FAILED(hr)) {
            pMoniker->Release();
            continue;
        }
        VARIANT var;
        VariantInit(&var);

        // Get the friendly name of the device
        if (SUCCEEDED(pPropBag->Read(L"FriendlyName", &var, 0))) {
            std::wstring deviceName = var.bstrVal;
            VariantClear(&var);
            deviceNames.push_back(deviceName);
        }

        pPropBag->Release();
        pMoniker->Release();
    }
    pEnum->Release();
    pDevEnum->Release();

    return (int)deviceNames.size();
}

PYBIND11_MODULE(win32DeviceEnumBind, m) {
    m.def("InitializeCOM", &InitializeCOM, "A function that initializes COM");
    m.def("UninitializeCOM", &UninitializeCOM, "A function that uninitializes COM");
    m.def("EnumerateVideoDevicesDShow", []() {
        std::vector<std::wstring> deviceNames;
        EnumerateVideoDevicesDShow(deviceNames);
        return deviceNames;
    }, "A function that enumerates video devices");
}
