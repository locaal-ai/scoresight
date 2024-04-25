from os import path
import platform
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer
from PySide6.QtUiTools import QUiLoader
from sc_logging import log_file_path
from ui_log_view import Ui_Dialog as Ui_LogViewerDialog


class LogViewerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LogViewerDialog()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(1000)  # Update UI every 1 second
        self.current_log_data = ""
        self.ui.pushButton_openlogfolder.clicked.connect(self.open_log_folder)

    def open_log_folder(self):
        # Open the folder containing the log file
        # check if this is windows, mac or linux
        if path.exists(log_file_path):
            os_name = platform.system()

            if os_name == "Windows":
                from os import startfile

                startfile(path.dirname(log_file_path))
            elif os_name == "Linux":
                import subprocess

                subprocess.Popen(["xdg-open", path.dirname(log_file_path)])
            elif os_name == "Darwin":
                import subprocess

                subprocess.Popen(["open", path.dirname(log_file_path)])

    def update_ui(self):
        with open(log_file_path, "r") as log_file:
            lines = log_file.readlines()
            last_1000_lines = lines[-1000:]
            log_data = "".join(last_1000_lines)
            if log_data == self.current_log_data:
                return
            self.current_log_data = log_data
            # Update the UI with the log data
            self.ui.textEdit_log.setPlainText(log_data)
            if self.ui.checkBox_autoScroll.isChecked():
                # scroll to the bottom
                self.ui.textEdit_log.verticalScrollBar().setValue(
                    self.ui.textEdit_log.verticalScrollBar().maximum()
                )
                self.ui.scrollArea.ensureWidgetVisible(self.ui.textEdit_log)
