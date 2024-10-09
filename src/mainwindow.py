from functools import partial
import os
import platform
import datetime
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMenu,
    QMessageBox,
    QTableWidgetItem,
)
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import (
    Qt,
    Signal,
    Slot,
    QTranslator,
    QObject,
    QCoreApplication,
    QEvent,
    QMetaMethod,
    QUrl,
)
from dotenv import load_dotenv
from os import path
from platformdirs import user_data_dir

from api_output import update_out_api
from box_settings_ui_handler import BoxSettingsUIHandler
from camera_info import CameraInfo
from get_camera_info import get_camera_info
from http_server import start_http_server, update_http_server
from ocr_training_data import OCRTrainingDataDialog
from resource_path import resource_path
from screen_capture_source import ScreenCapture
from source_view import ImageViewer
from defaults import (
    default_boxes,
    default_info_for_box_name,
    normalize_settings_dict,
)

from storage import (
    TextDetectionTargetMemoryStorage,
    fetch_data,
    remove_data,
    store_data,
    store_custom_box_name,
    rename_custom_box_name_in_storage,
    remove_custom_box_name_in_storage,
    fetch_custom_box_names,
)
from obs_websocket import (
    create_obs_scene_from_export,
    open_obs_websocket,
    update_text_source,
)

from template_fields import evaluate_template_field
from text_detection_target import TextDetectionTarget, TextDetectionTargetWithResult
from sc_logging import logger
from uno_ui_handler import UNOUIHandler
from update_check import check_for_updates
from log_view import LogViewerDialog
import file_output
from video_settings import VideoSettingsDialog
from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_Dialog as Ui_About
from ui_connect_obs import Ui_Dialog as Ui_ConnectObs
from ui_url_source import Ui_Dialog as Ui_UrlSource
from ui_screen_capture import Ui_Dialog as Ui_ScreenCapture
from vmix_ui_handler import VMixUIHanlder


def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
            widget = None
        else:
            clear_layout(item.layout())


class MainWindow(QMainWindow):
    # add a signal to update sources
    update_sources = Signal(list)
    get_sources = Signal()

    def __init__(self, translator: QTranslator, parent: QObject):
        super(MainWindow, self).__init__()
        self.parent_object = parent
        self.ui = Ui_MainWindow()
        logger.info("Starting ScoreSight")
        self.ui.setupUi(self)
        self.translator = translator
        # load env variables
        load_dotenv()
        self.setWindowTitle(f"ScoreSight - v{os.getenv('LOCAL_RELEASE_TAG')}")
        if platform.system() == "Windows":
            # set the icon
            self.setWindowIcon(QIcon(resource_path("icons", "Windows-icon-open.ico")))

        self.menubar = self.menuBar()
        file_menu = self.menubar.addMenu("File")

        # check for updates
        check_for_updates(False)
        file_menu.addAction("Check for Updates", lambda: check_for_updates(True))
        file_menu.addAction("About", self.openAboutDialog)
        file_menu.addAction("View Current Log", self.openLogsDialog)
        file_menu.addAction("Import Configuration", self.importConfiguration)
        file_menu.addAction("Export Configuration", self.exportConfiguration)
        file_menu.addAction("Open Configuration Folder", self.openConfigurationFolder)
        file_menu.addAction("OCR Training Data Setup", self.openOCRTrainingDataDialog)

        # Add "Language" menu
        languageMenu = file_menu.addMenu("Language")

        # Add language options
        self.addLanguageOption(languageMenu, "English (US)", "en_US")
        self.addLanguageOption(languageMenu, "French (France)", "fr_FR")
        self.addLanguageOption(languageMenu, "Spanish (Spain)", "es_ES")
        self.addLanguageOption(languageMenu, "German", "de_DE")
        self.addLanguageOption(languageMenu, "Italian", "it_IT")
        self.addLanguageOption(languageMenu, "Japanese", "ja_JP")
        self.addLanguageOption(languageMenu, "Korean", "ko_KR")
        self.addLanguageOption(languageMenu, "Dutch", "nl_NL")
        self.addLanguageOption(languageMenu, "Polish", "pl_PL")
        self.addLanguageOption(languageMenu, "Portuguese (Brazil)", "pt_BR")
        self.addLanguageOption(languageMenu, "Portuguese (Portugal)", "pt_PT")
        self.addLanguageOption(languageMenu, "Russian", "ru_RU")
        self.addLanguageOption(languageMenu, "Chinese (Simplified)", "zh_CN")

        # Hide the menu bar by default
        self.menubar.setVisible(False)

        # Show the menu bar when the Alt key is pressed
        self.installEventFilter(self)

        self.ui.pushButton_connectObs.clicked.connect(self.openOBSConnectModal)

        self.vmixUiHandler = VMixUIHanlder(self.ui)
        self.unoUiHandler = UNOUIHandler(self.ui)
        self.boxSettingsUiHandler = BoxSettingsUIHandler(self.ui)

        self.ui.checkBox_templatefield.toggled.connect(self.makeTemplateField)

        start_http_server()

        self.ui.pushButton_stabilize.setEnabled(True)
        self.ui.pushButton_stabilize.clicked.connect(self.toggleStabilize)

        self.ui.toolButton_topCrop.clicked.connect(self.cropMode)
        # check configuation if crop is enabled
        self.ui.toolButton_topCrop.setChecked(
            fetch_data("scoresight.json", "crop_mode", False)
        )
        self.ui.widget_cropPanel.setVisible(self.ui.toolButton_topCrop.isChecked())
        self.ui.widget_cropPanel.setEnabled(self.ui.toolButton_topCrop.isChecked())
        self.ui.spinBox_leftCrop.valueChanged.connect(
            partial(self.globalSettingsChanged, "left_crop")
        )
        self.ui.spinBox_leftCrop.setValue(fetch_data("scoresight.json", "left_crop", 0))
        self.ui.spinBox_rightCrop.valueChanged.connect(
            partial(self.globalSettingsChanged, "right_crop")
        )
        self.ui.spinBox_rightCrop.setValue(
            fetch_data("scoresight.json", "right_crop", 0)
        )
        self.ui.spinBox_topCrop.valueChanged.connect(
            partial(self.globalSettingsChanged, "top_crop")
        )
        self.ui.spinBox_topCrop.setValue(fetch_data("scoresight.json", "top_crop", 0))
        self.ui.spinBox_bottomCrop.valueChanged.connect(
            partial(self.globalSettingsChanged, "bottom_crop")
        )
        self.ui.spinBox_bottomCrop.setValue(
            fetch_data("scoresight.json", "bottom_crop", 0)
        )
        self.ui.checkBox_enableOutAPI.toggled.connect(
            partial(self.globalSettingsChanged, "enable_out_api")
        )
        self.ui.checkBox_enableOutAPI.setChecked(
            fetch_data("scoresight.json", "enable_out_api", False)
        )

        # connect toolButton_rotate
        self.ui.toolButton_rotate.clicked.connect(self.rotateImage)

        self.ui.widget_detectionCadence.setVisible(True)
        self.ui.horizontalSlider_detectionCadence.setValue(
            fetch_data("scoresight.json", "detection_cadence", 5)
        )
        self.ui.horizontalSlider_detectionCadence.valueChanged.connect(
            self.detectionCadenceChanged
        )
        self.ui.toolButton_addBox.clicked.connect(self.addBox)
        self.ui.toolButton_removeBox.clicked.connect(self.removeCustomBox)

        self.video_settings_dialog = None
        self.ui.toolButton_videoSettings.clicked.connect(self.openVideoSettings)

        self.ui.lineEdit_api_url.textChanged.connect(
            partial(self.globalSettingsChanged, "out_api_url")
        )
        self.ui.lineEdit_api_url.setText(
            fetch_data("scoresight.json", "out_api_url", "")
        )

        self.ui.checkBox_enableOutAPI.toggled.connect(
            partial(self.globalSettingsChanged, "enable_out_api")
        )
        self.ui.checkBox_enableOutAPI.setChecked(
            fetch_data("scoresight.json", "enable_out_api", False)
        )
        self.ui.comboBox_api_encode.currentTextChanged.connect(
            partial(self.globalSettingsChanged, "out_api_encoding")
        )
        self.ui.comboBox_api_encode.setCurrentIndex(
            self.ui.comboBox_api_encode.findText(
                fetch_data("scoresight.json", "out_api_encoding", "JSON")
            )
        )
        self.ui.comboBox_outApiMethod.currentTextChanged.connect(
            partial(self.globalSettingsChanged, "out_api_method")
        )
        self.ui.comboBox_outApiMethod.setCurrentIndex(
            self.ui.comboBox_outApiMethod.findText(
                fetch_data("scoresight.json", "out_api_method", "POST")
            )
        )

        self.obs_websocket_client = None

        ocr_models = [
            "Daktronics",
            "General Scoreboard",
            "General Fonts (English)",
            "General Scoreboard Large",
        ]
        self.ui.comboBox_ocrModel.addItems(ocr_models)
        self.ui.comboBox_ocrModel.setCurrentIndex(
            fetch_data("scoresight.json", "ocr_model", 1)
        )  # default to General Scoreboard

        self.ui.frame_source_view.setEnabled(False)
        self.ui.groupBox_target_settings.setEnabled(False)
        self.ui.pushButton_makeBox.clicked.connect(self.makeBox)
        self.ui.pushButton_removeBox.clicked.connect(self.removeBox)
        self.ui.tableWidget_boxes.itemClicked.connect(self.listItemClicked)
        # connect the edit triggers
        self.ui.tableWidget_boxes.itemDoubleClicked.connect(self.editBoxName)
        self.ui.pushButton_refresh_sources.clicked.connect(
            lambda: self.get_sources.emit()
        )
        self.detectionTargetsStorage = TextDetectionTargetMemoryStorage()
        self.detectionTargetsStorage.data_changed.connect(self.detectionTargetsChanged)
        self.ui.pushButton_createOBSScene.clicked.connect(self.createOBSScene)
        self.ui.pushButton_selectFolder.clicked.connect(self.selectOutputFolder)
        self.ui.toolButton_trashFolder.clicked.connect(self.clearOutputFolder)
        self.ui.pushButton_stopUpdates.toggled.connect(self.toggleStopUpdates)
        self.ui.comboBox_ocrModel.currentIndexChanged.connect(self.ocrModelChanged)
        self.ui.toolButton_zoomReset.clicked.connect(self.resetZoom)
        self.ui.toolButton_osd.toggled.connect(self.toggleOSD)
        self.ui.comboBox_boxDisplayStyle.currentIndexChanged.connect(
            partial(self.globalSettingsChanged, "box_display_style")
        )
        self.ui.comboBox_boxDisplayStyle.setCurrentIndex(
            fetch_data("scoresight.json", "box_display_style", 3)
        )

        self.ui.checkBox_updateOnchange.toggled.connect(self.toggleUpdateOnChange)

        # populate the tableWidget_boxes with the default and custom boxes
        custom_boxes_names = fetch_custom_box_names()

        for box_name in [box["name"] for box in default_boxes] + custom_boxes_names:
            item = QTableWidgetItem(
                QIcon(resource_path("icons", "circle-x.svg")),
                box_name,
            )
            item.setData(Qt.ItemDataRole.UserRole, "unchecked")
            self.ui.tableWidget_boxes.insertRow(self.ui.tableWidget_boxes.rowCount())
            self.ui.tableWidget_boxes.setItem(
                self.ui.tableWidget_boxes.rowCount() - 1, 0, item
            )
            disabledItem = QTableWidgetItem()
            disabledItem.setFlags(Qt.ItemFlag.NoItemFlags)
            self.ui.tableWidget_boxes.setItem(
                self.ui.tableWidget_boxes.rowCount() - 1, 1, disabledItem
            )

        self.image_viewer = None
        self.obs_connect_modal = None
        self.source_name = None
        self.updateOCRResults = True
        self.log_dialog = None
        if fetch_data("scoresight.json", "open_on_startup", False):
            logger.info("Opening log dialog on startup")
            self.openLogsDialog()

        if fetch_data("scoresight.json", "obs"):
            self.connectObs()

        self.out_folder = fetch_data("scoresight.json", "output_folder")
        if self.out_folder:
            if not path.exists(self.out_folder):
                self.out_folder = None
                remove_data("scoresight.json", "output_folder")
            else:
                self.ui.lineEdit_folder.setText(self.out_folder)

        self.first_csv_append = True
        self.last_aggregate_save = datetime.datetime.now()
        self.ui.checkBox_saveCsv.toggled.connect(
            partial(self.globalSettingsChanged, "save_csv")
        )
        self.ui.checkBox_saveCsv.setChecked(
            fetch_data("scoresight.json", "save_csv", False)
        )
        self.ui.checkBox_saveXML.toggled.connect(
            partial(self.globalSettingsChanged, "save_xml")
        )
        self.ui.checkBox_saveXML.setChecked(
            fetch_data("scoresight.json", "save_xml", False)
        )
        self.ui.comboBox_appendMethod.currentIndexChanged.connect(
            partial(self.globalSettingsChanged, "append_method")
        )
        self.ui.horizontalSlider_aggsPerSecond.valueChanged.connect(
            partial(self.globalSettingsChanged, "aggs_per_second")
        )
        self.ui.comboBox_appendMethod.setCurrentIndex(
            fetch_data("scoresight.json", "append_method", 3)
        )
        self.ui.horizontalSlider_aggsPerSecond.setValue(
            fetch_data("scoresight.json", "aggs_per_second", 5)
        )
        self.ui.checkBox_updateOnchange.setChecked(
            fetch_data("scoresight.json", "update_on_change", True)
        )
        self.ui.checkBox_vmix_send_same.setChecked(
            fetch_data("scoresight.json", "vmix_send_same", False)
        )
        self.ui.checkBox_vmix_send_same.toggled.connect(
            partial(self.globalSettingsChanged, "vmix_send_same")
        )

        self.ui.pushButton_saveOCRTrainingData.clicked.connect(self.saveOCRTrainingData)
        self.ui.pushButton_saveOCRTrainingData.setChecked(
            fetch_data("scoresight.json", "save_ocr_training_data", False)
        )

        self.ui.toolButton_speed.clicked.connect(self.toggleSpeed)

        self.update_sources.connect(self.updateSources)
        self.get_sources.connect(self.getSources)
        self.get_sources.emit()

    def toggleSpeed(self):
        # check the current speed and toggle it
        # possible speeds are x2, x4, x8, x16, x32 and back to x1
        # change the button text to the current speed
        # change the speed of the image viewer
        if self.image_viewer and self.image_viewer.timerThread is not None:
            speed = self.image_viewer.timerThread.getSpeed()
            if speed == 1:
                speed = 2
            elif speed == 2:
                speed = 4
            elif speed == 4:
                speed = 8
            elif speed == 8:
                speed = 16
            elif speed == 16:
                speed = 32
            else:
                speed = 1
            self.image_viewer.timerThread.setSpeed(speed)
            self.ui.toolButton_speed.setText(f"x{speed}")

    def saveOCRTrainingData(self):
        self.globalSettingsChanged(
            "save_ocr_training_data", self.ui.pushButton_saveOCRTrainingData.isChecked()
        )

    def openVideoSettings(self):
        # only allow opening the video settings for an OpenCV type source
        if not self.image_viewer or self.image_viewer is None:
            return

        if self.image_viewer.getCameraInfo().type != CameraInfo.CameraType.OPENCV:
            return

        if self.video_settings_dialog is None:
            # open the logs dialog
            self.video_settings_dialog = VideoSettingsDialog()
            self.video_settings_dialog.setWindowTitle("Video Settings")

        self.video_settings_dialog.init_ui(self.image_viewer.getCameraCapture())

        # show the dialog, non modal
        self.video_settings_dialog.show()

    def rotateImage(self):
        # store the rotation in the scoresight.json
        rotation = fetch_data("scoresight.json", "rotation", 0)
        rotation += 90
        if rotation >= 360:
            rotation = 0
        self.globalSettingsChanged("rotation", rotation)

    def cropMode(self):
        # if the toolButton_topCrop is unchecked, go to crop mode
        if self.ui.toolButton_topCrop.isChecked():
            self.ui.widget_cropPanel.setVisible(True)
            self.ui.widget_cropPanel.setEnabled(True)
            self.globalSettingsChanged("crop_mode", True)
        else:
            self.ui.widget_cropPanel.setVisible(False)
            self.ui.widget_cropPanel.setEnabled(False)
            self.globalSettingsChanged("crop_mode", False)

    def globalSettingsChanged(self, settingName, value):
        store_data("scoresight.json", settingName, value)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Alt:
                self.menubar.setVisible(True)
            if event.key() == Qt.Key_Escape:
                self.menubar.setVisible(False)
                # deselect any selected item
                self.itemSelected(None)
                if self.image_viewer is not None:
                    self.image_viewer.selectBox(None)
        elif event.type() == QEvent.FocusOut and self.menubar.isVisible():
            self.menubar.setVisible(False)
        elif event.type() == QEvent.WindowDeactivate and self.menubar.isVisible():
            self.menubar.setVisible(False)
        return super().eventFilter(obj, event)

    def focusOutEvent(self, event):
        if self.menubar.isVisible():
            self.menubar.setVisible(False)
        super().focusOutEvent(event)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowDeactivate and self.menubar.isVisible():
            self.menubar.setVisible(False)
        super().changeEvent(event)

    def changeLanguage(self, locale):
        locale_file = resource_path("translations", f"scoresight_{locale}.qm")
        logger.info(f"Changing language to {locale_file}")
        if not self.translator.load(locale_file):
            logger.error(f"Could not load translation for {locale_file}")
            return
        appInstance = QApplication.instance()
        if appInstance:
            logger.info(f"installing translator for {locale}")
            appInstance.installTranslator(self.translator)
            try:
                self.ui.retranslateUi(self)
            except Exception as e:
                logger.error(f"Error retranslating UI: {e}")

    def addLanguageOption(self, menu: QMenu, language_name: str, locale: str):
        menu.addAction(language_name, lambda: self.changeLanguage(locale))

    def toggleUpdateOnChange(self, value):
        self.globalSettingsChanged("update_on_change", value)
        if self.image_viewer:
            self.image_viewer.setUpdateOnChange(value)

    def importConfiguration(self):
        # open a file dialog to select a configuration file
        file, _ = QFileDialog.getOpenFileName(
            self, "Open Configuration File", "", "Configuration Files (*.json)"
        )
        if not file:
            return
        # load the configuration from the file
        if not self.detectionTargetsStorage.loadBoxesFromFile(file):
            # show an error qmessagebox
            logger.error("Error loading configuration file")
            QMessageBox.critical(
                self,
                "Error",
                "Error loading configuration file",
                QMessageBox.StandardButton.Ok,
            )
            return

    def exportConfiguration(self):
        # open a file dialog to select the output file
        file, _ = QFileDialog.getSaveFileName(
            self, "Save Configuration File", "", "Configuration Files (*.json)"
        )
        if not file:
            return
        # save the configuration to the file
        self.detectionTargetsStorage.saveBoxesToFile(file)

    def openOCRTrainingDataDialog(self):
        # open the OCR training data dialog
        dialog = OCRTrainingDataDialog()
        dialog.setWindowTitle("OCR Training Data Setup")
        dialog.exec()

    def openConfigurationFolder(self):
        # open the configuration folder in the file explorer
        QDesktopServices.openUrl(
            QUrl(
                "file:///" + user_data_dir("scoresight"), QUrl.ParsingMode.TolerantMode
            )
        )

    def toggleOSD(self, value):
        if self.image_viewer:
            self.image_viewer.toggleOSD(value)

    def resetZoom(self):
        if self.image_viewer:
            self.image_viewer.resetZoom()

    def detectionCadenceChanged(self, detections_per_second):
        self.globalSettingsChanged("detection_cadence", detections_per_second)
        if self.image_viewer and self.image_viewer.timerThread:
            # convert the detections_per_second to milliseconds
            self.image_viewer.timerThread.update_frame_interval = (
                1000 / detections_per_second
            )

    def ocrModelChanged(self, index):
        self.globalSettingsChanged("ocr_model", index)
        # update the ocr model in the text detector
        if (
            self.image_viewer
            and self.image_viewer.timerThread
            and self.image_viewer.timerThread.textDetector
        ):
            self.image_viewer.timerThread.textDetector.setOcrModel(index)

    def openLogsDialog(self):
        if self.log_dialog is None:
            # open the logs dialog
            self.log_dialog = LogViewerDialog()
            self.log_dialog.setWindowTitle("Logs")

        # show the dialog, non modal
        self.log_dialog.show()

    def openAboutDialog(self):
        # open the about dialog
        about_dialog = QDialog()
        about_dialog_ui = Ui_About()
        about_dialog_ui.setupUi(about_dialog)
        about_dialog.setWindowTitle("About ScoreSight")
        about_dialog.exec()

    def toggleStabilize(self):
        if not self.image_viewer:
            return
        # start or stop the stabilization
        self.image_viewer.toggleStabilization(self.ui.pushButton_stabilize.isChecked())

    def toggleStopUpdates(self, value):
        self.updateOCRResults = not value
        # change the text on the button
        self.ui.pushButton_stopUpdates.setText(
            self.translator.translate("MainWindow", "Resume Updates")
            if value
            else self.translator.translate("MainWindow", "Stop Updates")
        )

    def selectOutputFolder(self):
        # open a Qt dialog to select the output folder
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder",
            fetch_data("scoresight.json", "output_folder", ""),
            options=QFileDialog.Option.ShowDirsOnly,
        )
        if folder and len(folder) > 0:
            self.ui.lineEdit_folder.setText(folder)
            self.out_folder = folder
            self.globalSettingsChanged("output_folder", folder)

    def clearOutputFolder(self):
        # clear the output folder
        self.ui.lineEdit_folder.setText("")
        self.out_folder = None
        remove_data("scoresight.json", "output_folder")

    def detectionTargetsChanged(self, detectionTargets: list[TextDetectionTarget]):
        for box in detectionTargets:
            logger.debug(f"Change: Detection target: {box.name}")
            # change the list icon to green checkmark
            items = self.ui.tableWidget_boxes.findItems(
                box.name, Qt.MatchFlag.MatchExactly
            )
            if len(items) == 0:
                logger.warning(f"Item not found: {box.name}. Adding it to the list.")
                # add the item to the list
                self.ui.tableWidget_boxes.insertRow(
                    self.ui.tableWidget_boxes.rowCount()
                )
                item = QTableWidgetItem(box.name)
                self.ui.tableWidget_boxes.setItem(
                    self.ui.tableWidget_boxes.rowCount() - 1, 0, item
                )
                disabledItem = QTableWidgetItem()
                disabledItem.setFlags(Qt.ItemFlag.NoItemFlags)
                self.ui.tableWidget_boxes.setItem(
                    self.ui.tableWidget_boxes.rowCount() - 1, 1, disabledItem
                )
            else:
                item = items[0]

            if box.settings is None or not box.settings["templatefield"]:
                # this is a detection target
                item.setIcon(QIcon(resource_path("icons", "circle-check.svg")))
                item.setData(Qt.ItemDataRole.UserRole, "checked")
            else:
                # this is a template field
                item.setIcon(QIcon(resource_path("icons", "template-field.svg")))
                item.setData(Qt.ItemDataRole.UserRole, "templatefield")

        self.vmixUiHandler.updatevMixTable(detectionTargets)
        self.unoUiHandler.updateUNOTable(detectionTargets)

        # if save_csv is enabled, truncate the aggregate file
        if self.ui.checkBox_saveCsv.isChecked() and self.out_folder:
            csv_output_file_path = path.abspath(
                path.join(self.out_folder, "results.csv")
            )
            try:
                with open(csv_output_file_path, "w") as f:
                    f.write("")
                self.first_csv_append = True
                self.last_aggregate_save = datetime.datetime.now()
            except Exception as e:
                logger.error(f"Error truncating aggregate file: {e}")

    def listItemClicked(self, item):
        user_role = item.data(Qt.ItemDataRole.UserRole)
        if user_role in ["checked", "templatefield"] and item.column() == 0:
            # enable the remove box button and disable the make box button
            self.ui.pushButton_makeBox.setEnabled(False)
            self.ui.pushButton_removeBox.setEnabled(user_role == "checked")
            self.ui.groupBox_target_settings.setEnabled(user_role == "checked")
            self.boxSettingsUiHandler.populateSettings(item.text())
        else:
            # enable the make box button and disable the remove box button
            self.ui.pushButton_removeBox.setEnabled(False)
            self.ui.pushButton_makeBox.setEnabled(item.column() == 0)
            self.ui.groupBox_target_settings.setEnabled(False)
            self.boxSettingsUiHandler.populateSettings("")

        if item.column() == 0:
            # if this is not a default box - enable the template field checkbox
            if item.text() not in [box["name"] for box in default_boxes]:
                self.ui.checkBox_templatefield.setEnabled(True)
                self.ui.lineEdit_templatefield.setEnabled(True)
            else:
                self.ui.checkBox_templatefield.setEnabled(False)
                self.ui.lineEdit_templatefield.setEnabled(False)

        # notify the image viewer to select the box
        if self.image_viewer:
            self.image_viewer.selectBox(item.text())

    def openOBSConnectModal(self):
        # disable OBS options
        self.ui.lineEdit_sceneName.setEnabled(False)
        self.ui.checkBox_recreate.setEnabled(False)
        self.ui.pushButton_createOBSScene.setEnabled(False)

        # load the ui from "connect_obs.ui"
        self.obs_modal_ui = Ui_ConnectObs()
        self.obs_connect_modal = QDialog()
        self.obs_modal_ui.setupUi(self.obs_connect_modal)
        self.obs_connect_modal.setWindowTitle("Connect to OBS")

        # connect the "connect" button to a function
        self.obs_modal_ui.pushButton_connect.clicked.connect(self.connectObs)

        # load the saved data from scoresight.json
        obs_data = fetch_data("scoresight.json", "obs")
        if obs_data:
            self.obs_modal_ui.lineEdit_ip.setText(obs_data["ip"])
            self.obs_modal_ui.lineEdit_port.setText(obs_data["port"])
            self.obs_modal_ui.lineEdit_password.setText(obs_data["password"])
        # show the modal
        self.obs_connect_modal.show()
        # focus the connect button
        self.obs_modal_ui.pushButton_connect.setFocus()

    def connectObs(self):
        # open a websocket connection to OBS using obs_websocket.py
        # enable the save button in the modal if the connection is successful
        if self.obs_connect_modal is not None:
            self.obs_websocket_client = open_obs_websocket(
                {
                    "ip": self.obs_modal_ui.lineEdit_ip.text(),
                    "port": self.obs_modal_ui.lineEdit_port.text(),
                    "password": self.obs_modal_ui.lineEdit_password.text(),
                }
            )
        else:
            self.obs_websocket_client = open_obs_websocket(
                fetch_data("scoresight.json", "obs")
            )
        if not self.obs_websocket_client:
            # show error in label_error
            if self.obs_connect_modal:
                self.obs_modal_ui.label_error.setText("Cannot connect to OBS")
            return

        # connection was successful
        if self.obs_connect_modal:
            store_data(
                "scoresight.json",
                "obs",
                {
                    "ip": self.obs_modal_ui.lineEdit_ip.text(),
                    "port": self.obs_modal_ui.lineEdit_port.text(),
                    "password": self.obs_modal_ui.lineEdit_password.text(),
                },
            )
            self.obs_connect_modal.close()

        self.ui.lineEdit_sceneName.setEnabled(True)
        self.ui.checkBox_recreate.setEnabled(True)
        self.ui.pushButton_createOBSScene.setEnabled(True)

        logger.info("OBS: Connected")

    @Slot()
    def getSources(self):
        self.update_sources.emit(get_camera_info())

    @Slot(list)
    def updateSources(self, camera_sources: list[CameraInfo]):
        self.reset_playing_source()
        # clear all the items after "Screen Capture"
        for i in range(4, self.ui.comboBox_camera_source.count()):
            self.ui.comboBox_camera_source.removeItem(4)

        # populate the combobox with the sources
        for source in camera_sources:
            self.ui.comboBox_camera_source.addItem(source.description, source)

        self.ui.comboBox_camera_source.setEnabled(True)
        currentIndexChangedSignal = QMetaMethod.fromSignal(
            self.ui.comboBox_camera_source.currentIndexChanged
        )
        if self.ui.comboBox_camera_source.isSignalConnected(currentIndexChangedSignal):
            self.ui.comboBox_camera_source.currentIndexChanged.disconnect()
        self.ui.comboBox_camera_source.currentIndexChanged.connect(self.sourceChanged)

        # enable the source view frame
        self.ui.frame_source_view.setEnabled(True)

        selected_source_from_storage = fetch_data("scoresight.json", "source_selected")
        if type(selected_source_from_storage) == str:
            logger.info(
                "Source selected from storage: %s", selected_source_from_storage
            )
            # check if the source is a file path
            if path.exists(selected_source_from_storage):
                logger.info("File exists: %s", selected_source_from_storage)
                self.ui.comboBox_camera_source.blockSignals(True)
                self.ui.comboBox_camera_source.setCurrentIndex(1)
                self.ui.comboBox_camera_source.blockSignals(False)
                self.source_name = selected_source_from_storage
                self.sourceSelectionSucessful()
            else:
                # select the last selected source
                self.ui.comboBox_camera_source.setCurrentText(
                    selected_source_from_storage
                )

    def reset_playing_source(self):
        if self.image_viewer:
            # remove the image viewer from the layout frame_for_source_view_label
            self.ui.frame_for_source_view_label.layout().removeWidget(self.image_viewer)
            self.image_viewer.close()
            self.image_viewer = None
        # add a label with markdown text
        label_select_source = QLabel("### Open a Camera or Load a File")
        label_select_source.setTextFormat(Qt.TextFormat.MarkdownText)
        label_select_source.setEnabled(False)
        label_select_source.setAlignment(Qt.AlignmentFlag.AlignCenter)
        clear_layout(self.ui.frame_for_source_view_label.layout())
        self.ui.frame_for_source_view_label.layout().addWidget(label_select_source)

    def sourceChanged(self, index):
        # get the source name from the combobox
        self.source_name = None
        self.ui.groupBox_sb_info.setEnabled(False)
        self.ui.tableWidget_boxes.setEnabled(False)
        self.ui.widget_viewTools.setEnabled(False)
        self.ui.widget_cropPanel.setEnabled(False)
        if self.ui.comboBox_camera_source.currentIndex() == 0:
            self.reset_playing_source()
            return
        elif self.ui.comboBox_camera_source.currentIndex() == 1:
            logger.info("Open File selection dialog")
            # open a file dialog to select a video file
            file, _ = QFileDialog.getOpenFileName(
                self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mov)"
            )
            if not file or not path.exists(file):
                # no file selected - change source to "Select a source"
                logger.error("No file selected")
                self.ui.comboBox_camera_source.setCurrentText("Select a source")
                return
            else:
                logger.info("File selected: %s", file)
            self.source_name = file
        elif self.ui.comboBox_camera_source.currentIndex() == 2:
            # open a dialog to enter the url
            url_dialog = QDialog()
            ui_urlsource = Ui_UrlSource()
            ui_urlsource.setupUi(url_dialog)
            url_dialog.setWindowTitle("URL Source")
            # focus on url input
            ui_urlsource.lineEdit_url.setFocus()
            url_dialog.exec()  # wait for the dialog to close
            # check if the dialog was accepted
            if url_dialog.result() != QDialog.DialogCode.Accepted:
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
            self.source_name = ui_urlsource.lineEdit_url.text()
            if self.source_name == "":
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
        elif self.ui.comboBox_camera_source.currentIndex() == 3:
            # open a dialog to select the screen
            screen_dialog = QDialog()
            ui_screencapture = Ui_ScreenCapture()
            ui_screencapture.setupUi(screen_dialog)
            # set width and height of the dialog
            screen_dialog.setFixedWidth(400)

            screen_dialog.setWindowTitle(
                QCoreApplication.translate(
                    "MainWindow", "Screen Capture Selection", None
                )
            )
            # populate comboBox_window with the available windows
            ui_screencapture.comboBox_window.clear()
            ui_screencapture.comboBox_window.addItem(
                QCoreApplication.translate(
                    "MainWindow", "Capture the entire screen", None
                ),
                -1,
            )
            for window in ScreenCapture.list_windows():
                ui_screencapture.comboBox_window.addItem(window[0], window[1])
            screen_dialog.exec()
            # check if the dialog was accepted
            if screen_dialog.result() != QDialog.DialogCode.Accepted:
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
            # get the window ID from the comboBox_window
            window_id = ui_screencapture.comboBox_window.currentData()
            self.source_name = window_id

        # store the source selection in scoresight.json
        self.globalSettingsChanged("source_selected", self.source_name)
        self.sourceSelectionSucessful()

    def itemSelected(self, item_name):
        if item_name is None:
            # clear the selected item
            self.ui.tableWidget_boxes.clearSelection()
            self.ui.groupBox_target_settings.setEnabled(False)
            self.boxSettingsUiHandler.populateSettings("")
            return
        # select the item in the tableWidget_boxes
        items = self.ui.tableWidget_boxes.findItems(
            item_name, Qt.MatchFlag.MatchExactly
        )
        if len(items) == 0:
            return
        item = items[0]
        item.setSelected(True)
        self.ui.tableWidget_boxes.setCurrentItem(item)
        self.listItemClicked(item)

    def fourCornersApplied(self, corners):
        # check the button
        self.ui.pushButton_fourCorner.setChecked(True)

    def sourceSelectionSucessful(self):
        if self.ui.comboBox_camera_source.currentIndex() == 0:
            return

        self.ui.frame_source_view.setEnabled(False)

        if self.ui.comboBox_camera_source.currentIndex() == 1:
            if self.source_name is None or not path.exists(self.source_name):
                logger.error("No file selected")
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
            logger.info("Loading file selected: %s", self.source_name)
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.FILE,
            )
        elif self.ui.comboBox_camera_source.currentIndex() == 2:
            if self.source_name is None or self.source_name == "":
                logger.error("No url entered")
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
            logger.info("Loading url: %s", self.source_name)
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.URL,
            )
        elif self.ui.comboBox_camera_source.currentIndex() == 3:
            if self.source_name is None:
                logger.error("No screen capture selected")
                self.ui.comboBox_camera_source.setCurrentIndex(0)
                return
            logger.info("Loading screen capture: %s", self.source_name)
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.SCREEN_CAPTURE,
            )
        else:
            if self.ui.comboBox_camera_source.currentData() is None:
                return

            logger.info(
                "Loading camera: %s", self.ui.comboBox_camera_source.currentText()
            )
            camera_info = self.ui.comboBox_camera_source.currentData()

        if self.image_viewer:
            # remove the image viewer from the layout frame_for_source_view_label
            self.ui.frame_for_source_view_label.layout().removeWidget(self.image_viewer)
            self.image_viewer.close()
            self.image_viewer = None

        # clear self.ui.frame_for_source_view_label
        clear_layout(self.ui.frame_for_source_view_label.layout())

        # set the pixmap to the image viewer
        self.image_viewer = ImageViewer(
            camera_info,
            self.fourCornersApplied,
            self.detectionTargetsStorage,
            self.itemSelected,
        )
        self.ui.toolButton_videoSettings.setEnabled(
            camera_info.type == CameraInfo.CameraType.OPENCV
        )
        self.image_viewer.first_frame_received_signal.connect(
            self.cameraConnectedEnableUI
        )
        self.image_viewer.error_signal.connect(self.updateError)
        self.ocrModelChanged(fetch_data("scoresight.json", "ocr_model", 1))

        # set the image viewer to the layout frame_for_source_view_label
        self.ui.frame_for_source_view_label.layout().addWidget(self.image_viewer)

    def cameraConnectedEnableUI(self):
        if self.image_viewer is None:
            self.updateError("Image viewer is None")
            return
        self.ui.pushButton_fourCorner.toggled.connect(
            self.image_viewer.toggleFourCorner
        )
        self.ui.pushButton_binary.clicked.connect(self.image_viewer.toggleBinary)
        if self.image_viewer.timerThread:
            self.image_viewer.timerThread.ocr_result_signal.connect(self.ocrResult)
            self.image_viewer.timerThread.update_error.connect(self.updateError)

        # enable groupBox_sb_info
        self.ui.groupBox_sb_info.setEnabled(True)
        self.ui.tableWidget_boxes.setEnabled(True)
        self.ui.frame_source_view.setEnabled(True)
        self.ui.widget_viewTools.setEnabled(True)
        self.ui.widget_cropPanel.setEnabled(True)

        # load the boxes from scoresight.json
        self.detectionTargetsStorage.loadBoxesFromStorage()
        self.updateError(None)

    def updateError(self, error):
        if not error:
            return
        logger.error(error)
        self.ui.frame_source_view.setEnabled(True)
        self.ui.widget_viewTools.setEnabled(False)
        self.ui.widget_cropPanel.setEnabled(False)

    def ocrResult(self, results: list[TextDetectionTargetWithResult]):
        # update template fields
        for targetWithResult in results:
            if not targetWithResult.settings["templatefield"]:
                continue
            template_result = evaluate_template_field(results, targetWithResult)
            targetWithResult.result = (
                template_result if template_result is not None else ""
            )
            targetWithResult.result_state = (
                TextDetectionTargetWithResult.ResultState.Success
                if targetWithResult.result is not None
                else TextDetectionTargetWithResult.ResultState.Empty
            )

        # update the table widget value items
        for targetWithResult in results:
            if (
                targetWithResult.result_state
                == TextDetectionTargetWithResult.ResultState.Success
            ):
                items = self.ui.tableWidget_boxes.findItems(
                    targetWithResult.name, Qt.MatchFlag.MatchExactly
                )
                if len(items) == 0:
                    continue
                item = items[0]
                # get the value (1 column) of the item
                item = self.ui.tableWidget_boxes.item(item.row(), 1)
                item.setText(targetWithResult.result)

        if not self.updateOCRResults:
            # don't update the results, the user has disabled updates
            return

        update_http_server(results)

        if self.ui.checkBox_enableOutAPI.isChecked():
            update_out_api(results)

        # update vmix and uno
        if self.vmixUiHandler.vmixUpdater is not None:
            self.vmixUiHandler.vmixUpdater.update_vmix(results)
        if self.unoUiHandler.unoUpdater is not None:
            self.unoUiHandler.unoUpdater.update_uno(results)

        if self.out_folder is None:
            return

        if not path.exists(path.abspath(self.out_folder)):
            self.out_folder = None
            remove_data("scoresight.json", "output_folder")
            logger.warning("Output folder does not exist")
            return

        # check if enough time has passed since last file save according to aggs per second
        if (
            datetime.datetime.now() - self.last_aggregate_save
        ).total_seconds() < 1.0 / self.ui.horizontalSlider_aggsPerSecond.value():
            return

        self.last_aggregate_save = datetime.datetime.now()

        # update the obs scene sources with the results, use update_text_source
        for targetWithResult in results:
            if targetWithResult.result is None:
                continue
            if (
                targetWithResult.settings is not None
                and "skip_empty" in targetWithResult.settings
                and targetWithResult.settings["skip_empty"]
                and len(targetWithResult.result) == 0
            ):
                continue
            if (
                targetWithResult.result_state
                != TextDetectionTargetWithResult.ResultState.Success
            ):
                continue

            if (
                self.obs_websocket_client is not None
                and targetWithResult.settings is not None
            ):
                # find the source name for the target from the default boxes
                update_text_source(
                    self.obs_websocket_client,
                    targetWithResult.settings["obs_source_name"],
                    targetWithResult.result,
                )

        # save the results to text files
        file_output.save_text_files(
            results, self.out_folder, self.ui.comboBox_appendMethod.currentIndex()
        )

        # save the results to a csv file
        if self.ui.checkBox_saveCsv.isChecked():
            file_output.save_csv(
                results,
                self.out_folder,
                self.ui.comboBox_appendMethod.currentIndex(),
                self.first_csv_append,
            )

        # save the results to an xml file
        if self.ui.checkBox_saveXML.isChecked():
            file_output.save_xml(
                results,
                self.out_folder,
            )

    def addBox(self):
        # add a new box to the tableWidget_boxes
        # find the number of custom boxes
        custom_boxes = []
        for i in range(self.ui.tableWidget_boxes.rowCount()):
            item = self.ui.tableWidget_boxes.item(i, 0)
            if item.text() not in [o["name"] for o in default_boxes]:
                custom_boxes.append(item.text())

        i = len(custom_boxes)
        new_box_name = f"Custom {i + 1}"
        custom_boxes_names = fetch_data("scoresight.json", "custom_boxes_names", [])
        # find if the name already exists
        while new_box_name in custom_boxes or new_box_name in custom_boxes_names:
            i += 1
            new_box_name = f"Custom {i + 1}"

        store_custom_box_name(new_box_name)
        item = QTableWidgetItem(
            QIcon(resource_path("icons", "circle-x.svg")),
            new_box_name,
        )
        item.setData(Qt.ItemDataRole.UserRole, "unchecked")
        self.ui.tableWidget_boxes.insertRow(self.ui.tableWidget_boxes.rowCount())
        self.ui.tableWidget_boxes.setItem(
            self.ui.tableWidget_boxes.rowCount() - 1, 0, item
        )
        disabledItem = QTableWidgetItem()
        disabledItem.setFlags(Qt.ItemFlag.NoItemFlags)
        self.ui.tableWidget_boxes.setItem(
            self.ui.tableWidget_boxes.rowCount() - 1, 1, disabledItem
        )

    def removeCustomBox(self):
        item = self.ui.tableWidget_boxes.currentItem()
        if not item:
            logger.info("No item selected")
            return
        if item.column() != 0:
            item = self.ui.tableWidget_boxes.item(item.row(), 0)
        self.removeBox()
        remove_custom_box_name_in_storage(item.text())
        # only allow removing custom boxes
        if item.text() in [o["name"] for o in default_boxes]:
            logger.info("Cannot remove default box")
            return
        # remove the selected item from the tableWidget_boxes
        self.ui.tableWidget_boxes.removeRow(item.row())

    def editBoxName(self, item):
        if item.text() in [o["name"] for o in default_boxes]:
            # dont allow editing default boxes
            return
        new_name, ok = QInputDialog.getText(
            self, "Edit Box Name", "New Name:", text=item.text()
        )
        old_name = item.text()
        if ok and new_name != "" and new_name != old_name:
            # check if name doesn't exist already
            for i in range(self.ui.tableWidget_boxes.rowCount()):
                if new_name == self.ui.tableWidget_boxes.item(i, 0).text():
                    logger.info("Name '%s' already exists", new_name)
                    return
            # rename the item in the tableWidget_boxes
            rename_custom_box_name_in_storage(old_name, new_name)
            item.setText(new_name)
            # rename the item in the detectionTargetsStorage
            if not self.detectionTargetsStorage.rename_item(old_name, new_name):
                logger.info("Error renaming item in application storage")
                return
            else:
                # check if the item role isn't "templatefield"
                if item.data(Qt.ItemDataRole.UserRole) != "templatefield":
                    # remove the item from the tableWidget_boxes
                    self.ui.tableWidget_boxes.removeRow(item.row())

    def makeBox(self):
        item = self.ui.tableWidget_boxes.currentItem()
        if not item:
            return
        # create a new box on self.image_viewer with the name of the selected item from the tableWidget_boxes
        # change the list icon to green checkmark
        item.setIcon(QIcon(resource_path("icons/circle-check.svg")))
        item.setData(Qt.ItemDataRole.UserRole, "checked")
        self.listItemClicked(item)

        # get the size of the box from the name
        info = default_info_for_box_name(item.text())

        self.detectionTargetsStorage.add_item(
            TextDetectionTarget(
                info["x"],
                info["y"],
                info["width"],
                info["height"],
                item.text(),
                normalize_settings_dict({}, info),
            )
        )

    def removeBox(self):
        item = self.ui.tableWidget_boxes.currentItem()
        if not item:
            return
        # change the list icon to red x
        item.setIcon(QIcon(resource_path("icons", "circle-x.svg")))
        item.setData(Qt.ItemDataRole.UserRole, "unchecked")
        self.listItemClicked(item)
        self.detectionTargetsStorage.remove_item(item.text())

    def makeTemplateField(self, toggled: bool):
        item = self.ui.tableWidget_boxes.currentItem()
        if not item:
            return

        if not toggled:
            self.removeBox()
            return

        # create a new box on self.image_viewer with the name of the selected item from the tableWidget_boxes
        # change the list icon to green checkmark
        item.setIcon(QIcon(resource_path("icons", "template-field.svg")))
        item.setData(Qt.ItemDataRole.UserRole, "templatefield")

        self.detectionTargetsStorage.add_item(
            TextDetectionTarget(
                0,
                0,
                0,
                0,
                item.text(),
                normalize_settings_dict({"templatefield": True}, None),
            )
        )

        self.listItemClicked(item)

    def createOBSScene(self):
        # get the scene name from the lineEdit_sceneName
        scene_name = self.ui.lineEdit_sceneName.text()
        # clear or create a new scene
        create_obs_scene_from_export(self.obs_websocket_client, scene_name)

    # on destroy, close the OBS connection
    def closeEvent(self, event):
        logger.info("Closing")
        if self.image_viewer:
            self.image_viewer.close()
            self.image_viewer = None

        if self.log_dialog:
            self.log_dialog.close()
            self.log_dialog = None

        # store the boxes to scoresight.json
        self.detectionTargetsStorage.saveBoxesToStorage()
        if self.obs_websocket_client:
            # destroy the client object
            self.obs_websocket_client = None

        super().closeEvent(event)
