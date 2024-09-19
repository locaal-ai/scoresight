# -*- mode: python ; coding: utf-8 -*-
import os

# parse command line arguments
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mac_osx', action='store_true')
parser.add_argument('--win', action='store_true')
parser.add_argument('--debug', action='store_true')

args = parser.parse_args()

datas = [
    ('.env', '.'),
    ('icons/circle-check.svg', './icons'),
    ('icons/circle-x.svg', './icons'),
    ('icons/template-field.svg', './icons'),
    ('icons/MacOS_icon.png', './icons'),
    ('icons/plus.svg', './icons'),
    ('icons/splash.png', './icons'),
    ('icons/trash.svg', './icons'),
    ('icons/Windows-icon-open.ico', './icons'),
    ('tesseract/tessdata/daktronics.traineddata', './tesseract/tessdata'),
    ('tesseract/tessdata/scoreboard_general.traineddata', './tesseract/tessdata'),
    ('tesseract/tessdata/scoreboard_general_large.traineddata', './tesseract/tessdata'),
    ('tesseract/tessdata/eng.traineddata', './tesseract/tessdata'),
    ('obs_data/Scoresight_OBS_scene_collection.json', './obs_data'),
    ('obs_data/Scoreboard parts/Left Scoreboard.png', './obs_data/Scoreboard parts'),
    ('obs_data/Scoreboard parts/Left base Scoreboard.png', './obs_data/Scoreboard parts'),
    ('obs_data/Scoreboard parts/Middle Scoreboard.png', './obs_data/Scoreboard parts'),
    ('obs_data/Scoreboard parts/Right Scoreboard.png', './obs_data/Scoreboard parts'),
    ('obs_data/Scoreboard parts/Right base Scoreboard.png', './obs_data/Scoreboard parts'),
    ('obs_data/Scoreboard parts/logo-placeholder-image.png', './obs_data/Scoreboard parts'),
    ('translations/scoresight_de_DE.qm', './translations'),
    ('translations/scoresight_en_US.qm', './translations'),
    ('translations/scoresight_es_ES.qm', './translations'),
    ('translations/scoresight_fr_FR.qm', './translations'),
    ('translations/scoresight_it_IT.qm', './translations'),
    ('translations/scoresight_ja_JP.qm', './translations'),
    ('translations/scoresight_ko_KR.qm', './translations'),
    ('translations/scoresight_nl_NL.qm', './translations'),
    ('translations/scoresight_pl_PL.qm', './translations'),
    ('translations/scoresight_pt_BR.qm', './translations'),
    ('translations/scoresight_pt_PT.qm', './translations'),
    ('translations/scoresight_ru_RU.qm', './translations'),
    ('translations/scoresight_zh_CN.qm', './translations'),
]

sources = [
    'camera_info.py',
    'camera_view.py',
    'defaults.py',
    'file_output.py',
    'frame_stabilizer.py',
    'get_camera_info.py',
    'http_server.py',
    'log_view.py',
    'main.py',
    'ndi.py',
    'obs_websocket.py',
    'resizable_rect.py',
    'sc_logging.py',
    'screen_capture_source.py',
    'source_view.py',
    'storage.py',
    'tesseract.py',
    'text_detection_target.py',
    'video_settings.py',
    'ui_about.py',
    'ui_connect_obs.py',
    'ui_log_view.py',
    'ui_mainwindow.py',
    'ui_screen_capture.py',
    'ui_update_available.py',
    'ui_url_source.py',
    'ui_video_settings.py',
    'update_check.py',
    'vmix_output.py',
]

if args.win:
    datas += [('win32DeviceEnum/win32DeviceEnumBind.cp311-win_amd64.pyd', './win32DeviceEnum')]
    sources += ['win32DeviceEnum/enum_devices_dshow.py', 'screen_capture_source_windows.py']
if args.mac_osx:
    sources += ['screen_capture_source_mac.py']

a = Analysis(
    sources,
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['numpy.core.multiarray'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt6'],
    noarchive=False,
)
pyz = PYZ(a.pure)

if args.win:
    splash = Splash('icons/splash.png',
                    binaries=a.binaries,
                    datas=a.datas,
                    text_pos=(10, 20),
                    text_size=10,
                    text_color='black')
    exe = EXE(
        pyz,
        a.scripts,
        splash,
        name='scoresight',
        icon='icons/Windows-icon-open.ico',
        debug=args.debug is not None and args.debug,
        exclude_binaries=True,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        console=args.debug is not None and args.debug,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        splash.binaries,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='scoresight'
    )
elif args.mac_osx:
    exe = EXE(
        pyz,
        a.binaries,
        a.datas,
        a.scripts,
        name='scoresight',
        debug=args.debug is not None and args.debug,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=os.environ.get('APPLE_APP_DEVELOPER_ID', ''),
        entitlements_file='./entitlements.plist',
    )
    app = BUNDLE(
        exe,
        name='scoresight.app',
        icon='icons/MacOS_icon.png',
        bundle_identifier='com.royshilkrot.scoresight',
        version='0.0.1',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'NSCameraUsageDescription': 'Getting images from the camera to perform OCR'
        }
    )
else:
    splash = Splash('icons/splash.png',
                    binaries=a.binaries,
                    datas=a.datas,
                    text_pos=(10, 20),
                    text_size=10,
                    text_color='black')
    exe = EXE(
        pyz,
        a.binaries,
        a.datas,
        a.scripts,
        splash,
        splash.binaries,
        name='scoresight',
        icon='icons/Windows-icon-open.ico',
        debug=args.debug is not None and args.debug,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
    )
