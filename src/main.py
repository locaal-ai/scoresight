from os import path
import platform
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import (
    QTranslator,
    QLocale,
)

from mainwindow import MainWindow
from sc_logging import logger
from http_server import stop_http_server

if __name__ == "__main__":
    # only attempt splash when not on Mac OSX
    os_name = platform.system()
    if os_name != "Darwin":
        try:
            import pyi_splash  # type: ignore

            pyi_splash.close()
        except ImportError:
            pass
    app = QApplication(sys.argv)

    # Get system locale
    locale = QLocale.system().name()

    # Load the translation file based on the locale
    translator = QTranslator()
    locale_file = path.abspath(
        path.join(path.dirname(__file__), "..", "translations", f"scoresight_{locale}.qm")
    )
    # check if the file exists
    if not path.exists(locale_file):
        # load the default translation file
        locale_file = path.abspath(
            path.join(path.dirname(__file__), "..", "translations", "scoresight_en_US.qm")
        )
    if translator.load(locale_file):
        app.installTranslator(translator)

    # show the main window
    mainWindow = MainWindow(translator, app)
    mainWindow.show()

    app.exec()
    logger.info("Exiting...")

    stop_http_server()
