from functools import partial
import os
import platform
import sys
import datetime
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QLabel,
    QDialog,
    QInputDialog,
    QTableWidgetItem,
)
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from dotenv import load_dotenv
from os import path

from camera_info import CameraInfo
from get_camera_info import get_camera_info
from http_server import start_http_server, update_http_server, stop_http_server
from screen_capture_source import ScreenCapture
from source_view import ImageViewer
from defaults import (
    default_boxes,
    info_for_box_name,
    normalize_settings_dict,
    format_prefixes,
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

from text_detection_target import TextDetectionTarget, TextDetectionTargetWithResult
from sc_logging import logger
from update_check import check_for_updates
from log_view import LogViewerDialog
import file_output
from vmix_output import VMixAPI


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
    update_sources = pyqtSignal(list)
    get_sources = pyqtSignal()

    def __init__(self):
        super().__init__()
        path_to_dat = path.abspath(path.join(path.dirname(__file__), "mainwindow.ui"))
        loadUi(path_to_dat, self)
        # load env variables
        load_dotenv()
        self.setWindowTitle(
            f"{fetch_data('scoresight.json', 'product_name')} - v{os.getenv('LOCAL_RELEASE_TAG')} - Registered to: {fetch_data('scoresight.json', 'customer_name')}"
        )
        if platform.system() == "Windows":
            # set the icon
            self.setWindowIcon(
                QIcon(
                    path.abspath(
                        path.join(path.dirname(__file__), "icons/Windows-icon-open.ico")
                    )
                )
            )

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # check for updates
        check_for_updates(False)
        file_menu.addAction("Check for Updates", lambda: check_for_updates(True))
        file_menu.addAction("About", self.openAboutDialog)
        file_menu.addAction("View Current Log", self.openLogsDialog)

        file_menu.addAction("Import Configuration", self.importConfiguration)
        file_menu.addAction("Export Configuration", self.exportConfiguration)

        self.pushButton_connectObs.clicked.connect(self.openOBSConnectModal)
        self.statusbar.showMessage("OBS: Not Connected")

        self.vmixUiSetup()

        start_http_server()

        self.pushButton_stabilize.setEnabled(True)
        self.pushButton_stabilize.clicked.connect(self.toggleStabilize)

        self.widget_detectionCadence.setVisible(True)
        self.horizontalSlider_detectionCadence.setValue(
            fetch_data("scoresight.json", "detection_cadence", 5)
        )
        self.horizontalSlider_detectionCadence.valueChanged.connect(
            self.detectionCadenceChanged
        )
        self.toolButton_addBox.clicked.connect(self.addBox)
        self.toolButton_removeBox.clicked.connect(self.removeCustomBox)

        self.obs_websocket_client = None

        ocr_models = [
            "Daktronics",
            "General Scoreboard",
            "General Fonts (English)",
            "General Scoreboard Large",
        ]
        self.comboBox_ocrModel.addItems(ocr_models)
        self.comboBox_ocrModel.setCurrentIndex(
            fetch_data("scoresight.json", "ocr_model", 1)
        )  # default to General Scoreboard

        self.frame_source_view.setEnabled(False)
        self.groupBox_target_settings.setEnabled(False)
        self.pushButton_makeBox.clicked.connect(self.makeBox)
        self.pushButton_removeBox.clicked.connect(self.removeBox)
        self.tableWidget_boxes.itemClicked.connect(self.listItemClicked)
        # connect the edit triggers
        self.tableWidget_boxes.itemDoubleClicked.connect(self.editBoxName)
        self.pushButton_refresh_sources.clicked.connect(lambda: self.get_sources.emit())
        self.detectionTargetsStorage = TextDetectionTargetMemoryStorage()
        self.detectionTargetsStorage.data_changed.connect(self.detectionTargetsChanged)
        self.pushButton_createOBSScene.clicked.connect(self.createOBSScene)
        self.pushButton_selectFolder.clicked.connect(self.selectOutputFolder)
        self.toolButton_trashFolder.clicked.connect(self.clearOutputFolder)
        self.pushButton_stopUpdates.toggled.connect(self.toggleStopUpdates)
        self.comboBox_ocrModel.currentIndexChanged.connect(self.ocrModelChanged)
        self.pushButton_restoreDefaults.clicked.connect(self.restoreDefaults)
        self.toolButton_zoomReset.clicked.connect(self.resetZoom)
        self.toolButton_osd.toggled.connect(self.toggleOSD)
        self.toolButton_showOCRrects.toggled.connect(self.toggleOCRRects)
        self.checkBox_smoothing.toggled.connect(
            partial(self.genericSettingsChanged, "smoothing")
        )
        self.checkBox_skip_empty.toggled.connect(
            partial(self.genericSettingsChanged, "skip_empty")
        )
        self.horizontalSlider_conf_thresh.valueChanged.connect(self.confThreshChanged)
        self.lineEdit_format.textChanged.connect(
            partial(self.genericSettingsChanged, "format_regex")
        )
        self.comboBox_fieldType.currentIndexChanged.connect(
            partial(self.genericSettingsChanged, "type")
        )
        self.checkBox_skip_similar_image.toggled.connect(
            partial(self.genericSettingsChanged, "skip_similar_image")
        )
        self.checkBox_autocrop.toggled.connect(
            partial(self.genericSettingsChanged, "autocrop")
        )
        self.horizontalSlider_cleanup.valueChanged.connect(self.cleanupThreshChanged)
        self.horizontalSlider_dilate.valueChanged.connect(
            partial(self.genericSettingsChanged, "dilate")
        )
        self.horizontalSlider_skew.valueChanged.connect(
            partial(self.genericSettingsChanged, "skew")
        )
        self.horizontalSlider_vscale.valueChanged.connect(
            partial(self.genericSettingsChanged, "vscale")
        )
        self.checkBox_removeLeadingZeros.toggled.connect(
            partial(self.genericSettingsChanged, "remove_leading_zeros")
        )
        self.checkBox_rescalePatch.toggled.connect(
            partial(self.genericSettingsChanged, "rescale_patch")
        )
        self.checkBox_normWHRatio.toggled.connect(
            partial(self.genericSettingsChanged, "normalize_wh_ratio")
        )
        self.checkBox_invertPatch.toggled.connect(
            partial(self.genericSettingsChanged, "invert_patch")
        )
        self.checkBox_ordinalIndicator.toggled.connect(
            partial(self.genericSettingsChanged, "ordinal_indicator")
        )
        self.comboBox_binarizationMethod.currentIndexChanged.connect(
            partial(self.genericSettingsChanged, "binarization_method")
        )
        self.comboBox_formatPrefix.currentIndexChanged.connect(self.formatPrefixChanged)

        # populate the tableWidget_boxes with the default and custom boxes
        custom_boxes_names = fetch_custom_box_names()

        for box_name in [box["name"] for box in default_boxes] + custom_boxes_names:
            item = QTableWidgetItem(
                QIcon(
                    path.abspath(
                        path.join(path.dirname(__file__), "icons/circle-x.svg")
                    )
                ),
                box_name,
            )
            item.setData(Qt.ItemDataRole.UserRole, "unchecked")
            self.tableWidget_boxes.insertRow(self.tableWidget_boxes.rowCount())
            self.tableWidget_boxes.setItem(
                self.tableWidget_boxes.rowCount() - 1, 0, item
            )
            disabledItem = QTableWidgetItem()
            disabledItem.setFlags(Qt.ItemFlag.NoItemFlags)
            self.tableWidget_boxes.setItem(
                self.tableWidget_boxes.rowCount() - 1, 1, disabledItem
            )

        self.image_viewer = None
        self.obs_connect_modal = None
        self.source_name = None
        self.updateOCRResults = True
        self.log_dialog = None

        if fetch_data("scoresight.json", "obs"):
            self.connectObs()

        self.out_folder = fetch_data("scoresight.json", "output_folder")
        if self.out_folder:
            if not path.exists(self.out_folder):
                self.out_folder = None
                remove_data("scoresight.json", "output_folder")
            else:
                self.lineEdit_folder.setText(self.out_folder)

        self.first_csv_append = True
        self.last_aggregate_save = datetime.datetime.now()
        self.checkBox_saveCsv.toggled.connect(self.save_csv_toggled)
        self.checkBox_saveCsv.setChecked(
            fetch_data("scoresight.json", "save_csv", False)
        )
        self.checkBox_saveXML.toggled.connect(self.save_xml_toggled)
        self.checkBox_saveXML.setChecked(
            fetch_data("scoresight.json", "save_xml", False)
        )
        self.comboBox_appendMethod.currentIndexChanged.connect(self.appendMethodChanged)
        self.horizontalSlider_aggsPerSecond.valueChanged.connect(
            self.aggsPerSecondChanged
        )
        self.comboBox_appendMethod.setCurrentIndex(
            fetch_data("scoresight.json", "append_method", 3)
        )
        self.horizontalSlider_aggsPerSecond.setValue(
            fetch_data("scoresight.json", "aggs_per_second", 5)
        )

        self.update_sources.connect(self.updateSources)
        self.get_sources.connect(self.getSources)
        self.get_sources.emit()

    def formatPrefixChanged(self, index):
        if index == 12:
            return  # do nothing if "Select Preset" is selected
        # based on the selected index, set the format prefix
        # change lineEdit_format to the selected format prefix
        self.lineEdit_format.setText(format_prefixes[index])

    def importConfiguration(self):
        # open a file dialog to select a configuration file
        file, _ = QFileDialog.getOpenFileName(
            self, "Open Configuration File", "", "Configuration Files (*.json)"
        )
        if not file:
            return
        # load the configuration from the file
        if not self.detectionTargetsStorage.loadBoxesFromFile(file):
            # show an error message
            self.statusbar.showMessage("Error loading configuration file")

    def exportConfiguration(self):
        # open a file dialog to select the output file
        file, _ = QFileDialog.getSaveFileName(
            self, "Save Configuration File", "", "Configuration Files (*.json)"
        )
        if not file:
            return
        # save the configuration to the file
        self.detectionTargetsStorage.saveBoxesToFile(file)

    def toggleOSD(self, value):
        if self.image_viewer:
            self.image_viewer.toggleOSD(value)

    def toggleOCRRects(self, value):
        if self.image_viewer:
            self.image_viewer.toggleOCRRects(value)

    def save_csv_toggled(self, value):
        store_data("scoresight.json", "save_csv", value)

    def save_xml_toggled(self, value):
        store_data("scoresight.json", "save_xml", value)

    def appendMethodChanged(self, index):
        store_data("scoresight.json", "append_method", index)

    def aggsPerSecondChanged(self, value):
        store_data("scoresight.json", "aggs_per_second", value)

    def resetZoom(self):
        if self.image_viewer:
            self.image_viewer.resetZoom()

    def detectionCadenceChanged(self, detections_per_second):
        store_data("scoresight.json", "detection_cadence", detections_per_second)
        if self.image_viewer and self.image_viewer.timerThread:
            # convert the detections_per_second to milliseconds
            self.image_viewer.timerThread.update_frame_interval = (
                1000 / detections_per_second
            )

    def ocrModelChanged(self, index):
        store_data("scoresight.json", "ocr_model", index)
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
        loadUi(
            path.abspath(path.join(path.dirname(__file__), "about.ui")),
            about_dialog,
        )
        about_dialog.setWindowTitle("About ScoreSight")
        about_dialog.exec()

    def toggleStabilize(self):
        if not self.image_viewer:
            return
        # start or stop the stabilization
        self.image_viewer.toggleStabilization(self.pushButton_stabilize.isChecked())

    # def toggleHttpServer(self):
    #     if not self.pushButton_starthttpserver.isChecked():
    #         # stop the http server
    #         stop_http_server()
    #         # change the button text to "start the http server"
    #         self.pushButton_starthttpserver.setText("▶️ Start the server")
    #         return
    #     else:
    #         # start the http server
    #         start_http_server()
    #         # change the button text to "stop the http server"
    #         self.pushButton_starthttpserver.setText("🛑 Stop the server")

    def toggleStopUpdates(self, value):
        self.statusbar.showMessage("Stopped updates" if value else "Resumed updates")
        self.updateOCRResults = not value
        # change the text on the button
        self.pushButton_stopUpdates.setText(
            "▶️ Resume updates" if value else "🛑 Stop updates"
        )

    def selectOutputFolder(self):
        # open a Qt dialog to select the output folder
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder",
            fetch_data("scoresight.json", "output_folder"),
            options=QFileDialog.Option.ShowDirsOnly,
        )
        if folder and len(folder) > 0:
            self.lineEdit_folder.setText(folder)
            self.out_folder = folder
            store_data("scoresight.json", "output_folder", folder)

    def clearOutputFolder(self):
        # clear the output folder
        self.lineEdit_folder.setText("")
        self.out_folder = None
        remove_data("scoresight.json", "output_folder")

    def editSettings(self, settingsMutatorCallback):
        # update the selected item's settings in the detectionTargetsStorage
        item = self.tableWidget_boxes.currentItem()
        if not item:
            logger.info("no item selected")
            return
        item_name = item.text()
        item_obj = self.detectionTargetsStorage.find_item_by_name(item_name)
        if not item_obj:
            logger.info("item not found: %s", item_name)
            return
        item_obj = settingsMutatorCallback(item_obj)
        self.detectionTargetsStorage.edit_item(item_name, item_obj)

    def restoreDefaults(self):
        # restore the default settings for the selected item
        def restoreDefaultsSettings(item_obj):
            info = info_for_box_name(item_obj.name)
            item_obj.settings = normalize_settings_dict({}, info)
            return item_obj

        self.editSettings(restoreDefaultsSettings)
        self.populateSettings(self.tableWidget_boxes.currentItem().text())

    def confThreshChanged(self):
        def editConfThreshSettings(item_obj):
            item_obj.settings["conf_thresh"] = (
                float(self.horizontalSlider_conf_thresh.value()) / 100.0
            )
            return item_obj

        self.editSettings(editConfThreshSettings)

    def cleanupThreshChanged(self):
        def editCleanupThreshSettings(item_obj):
            item_obj.settings["cleanup_thresh"] = (
                float(self.horizontalSlider_cleanup.value()) / 100.0
            )
            return item_obj

        self.editSettings(editCleanupThreshSettings)

    def genericSettingsChanged(self, settingName, value):
        def editGenericSettings(item_obj):
            item_obj.settings[settingName] = value
            return item_obj

        self.editSettings(editGenericSettings)

    def vmixConnectionChanged(self):
        self.vmixUpdater = VMixAPI(
            self.lineEdit_vmixHost.text(),
            self.lineEdit_vmixPort.text(),
            self.inputLineEdit_vmix.text(),
            {},
        )
        store_data("scoresight.json", "vmix_host", self.lineEdit_vmixHost.text())
        store_data("scoresight.json", "vmix_port", self.lineEdit_vmixPort.text())
        store_data("scoresight.json", "vmix_input", self.inputLineEdit_vmix.text())

    def vmixMappingChanged(self, _):
        # store entire mapping data in scoresight.json
        mapping = {}
        for i in range(self.tableView_vmixMapping.model().rowCount()):
            item = self.tableView_vmixMapping.model().item(i, 0)
            value = self.tableView_vmixMapping.model().item(i, 1)
            if item and value:
                mapping[item.text()] = value.text()
        store_data("scoresight.json", "vmix_mapping", mapping)
        self.vmixUpdater.set_field_mapping(mapping)

    def vmixUiSetup(self):
        # populate the vmix connection from storage
        self.lineEdit_vmixHost.setText(
            fetch_data("scoresight.json", "vmix_host", "localhost")
        )
        self.lineEdit_vmixPort.setText(
            fetch_data("scoresight.json", "vmix_port", "8099")
        )
        self.inputLineEdit_vmix.setText(
            fetch_data("scoresight.json", "vmix_input", "1")
        )
        # connect the lineEdits to vmixConnectionChanged
        self.lineEdit_vmixHost.textChanged.connect(self.vmixConnectionChanged)
        self.lineEdit_vmixPort.textChanged.connect(self.vmixConnectionChanged)
        self.inputLineEdit_vmix.textChanged.connect(self.vmixConnectionChanged)

        # create the vmixUpdater
        self.vmixUpdater = VMixAPI(
            self.lineEdit_vmixHost.text(),
            self.lineEdit_vmixPort.text(),
            self.inputLineEdit_vmix.text(),
            {},
        )
        # add standard item model to the tableView_vmixMapping
        self.tableView_vmixMapping.setModel(QStandardItemModel())
        mapping = fetch_data("scoresight.json", "vmix_mapping", {})
        if mapping:
            self.vmixUpdater.set_field_mapping(mapping)

        self.tableView_vmixMapping.model().itemChanged.connect(self.vmixMappingChanged)

        self.pushButton_startvmix.toggled.connect(self.togglevMix)

    def togglevMix(self, value):
        if not self.vmixUpdater:
            return
        if value:
            self.pushButton_startvmix.setText("🛑 Stop vMix")
            self.vmixUpdater.running = True
        else:
            self.pushButton_startvmix.setText("▶️ Start vMix")
            self.vmixUpdater.running = False

    def updatevMixTable(self, detectionTargets):
        mapping_storage = fetch_data("scoresight.json", f"vmix_mapping")
        model = QStandardItemModel()
        model.blockSignals(True)

        for box in detectionTargets:
            # add the detection to the vmix output mapping: tableView_vmixMapping
            # check if the table already has the detectionTarget
            items = model.findItems(box.name, Qt.MatchFlag.MatchExactly)
            if len(items) == 0:
                # add the item to the list
                row = model.rowCount()
                model.insertRow(row)
                model.setItem(row, 0, QStandardItem(box.name))
                # the first item shouldn't be editable
                model.item(row, 0).setFlags(Qt.ItemFlag.NoItemFlags)
                if mapping_storage and box.name in mapping_storage:
                    model.setItem(row, 1, QStandardItem(mapping_storage[box.name]))
                else:
                    model.setItem(row, 1, QStandardItem(box.name))
            else:
                # update the item in the list
                item = items[0]
                row = item.row()
                # get value from storage
                if mapping_storage and box.name in mapping_storage:
                    model.setItem(row, 1, QStandardItem(mapping_storage[box.name]))
                else:
                    model.setItem(row, 1, QStandardItem(box.name))
        # remove the items that are not in the detectionTargets
        for i in range(model.rowCount()):
            item = model.item(i, 0)
            if not any([box.name == item.text() for box in detectionTargets]):
                model.removeRow(i)

        model.blockSignals(False)
        self.tableView_vmixMapping.setModel(model)

    def detectionTargetsChanged(self, detectionTargets):
        for box in detectionTargets:
            # change the list icon to green checkmark
            items = self.tableWidget_boxes.findItems(
                box.name, Qt.MatchFlag.MatchExactly
            )
            if len(items) == 0:
                # add the item to the list
                item = QTableWidgetItem(box.name)
                self.tableWidget_boxes.setItem(
                    self.tableWidget_boxes.rowCount(), 0, item
                )
            else:
                item = items[0]
            item.setIcon(
                QIcon(
                    path.abspath(
                        path.join(path.dirname(__file__), "icons/circle-check.svg")
                    )
                )
            )
            item.setData(Qt.ItemDataRole.UserRole, "checked")

        self.updatevMixTable(detectionTargets)

        # if save_csv is enabled, truncate the aggregate file
        if self.checkBox_saveCsv.isChecked() and self.out_folder:
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

    def populateSettings(self, name):
        self.lineEdit_format.blockSignals(True)
        self.comboBox_fieldType.blockSignals(True)
        self.checkBox_smoothing.blockSignals(True)
        self.checkBox_skip_empty.blockSignals(True)
        self.horizontalSlider_conf_thresh.blockSignals(True)
        self.checkBox_autocrop.blockSignals(True)
        self.checkBox_skip_similar_image.blockSignals(True)
        self.horizontalSlider_cleanup.blockSignals(True)
        self.horizontalSlider_dilate.blockSignals(True)
        self.horizontalSlider_skew.blockSignals(True)
        self.horizontalSlider_vscale.blockSignals(True)
        self.checkBox_removeLeadingZeros.blockSignals(True)
        self.checkBox_rescalePatch.blockSignals(True)
        self.checkBox_normWHRatio.blockSignals(True)
        self.checkBox_invertPatch.blockSignals(True)
        self.checkBox_ordinalIndicator.blockSignals(True)
        self.comboBox_binarizationMethod.blockSignals(True)
        self.comboBox_formatPrefix.blockSignals(True)

        # populate the settings from the detectionTargetsStorage
        item_obj = self.detectionTargetsStorage.find_item_by_name(name)
        if not item_obj:
            self.lineEdit_format.setText("")
            self.comboBox_fieldType.setCurrentIndex(0)
            self.checkBox_smoothing.setChecked(True)
            self.checkBox_skip_empty.setChecked(True)
            self.horizontalSlider_conf_thresh.setValue(50)
            self.checkBox_autocrop.setChecked(False)
            self.checkBox_skip_similar_image.setChecked(False)
            self.horizontalSlider_cleanup.setValue(0)
            self.horizontalSlider_dilate.setValue(1)
            self.horizontalSlider_skew.setValue(0)
            self.horizontalSlider_vscale.setValue(10)
            self.label_selectedInfo.setText("")
            self.checkBox_removeLeadingZeros.setChecked(False)
            self.checkBox_rescalePatch.setChecked(False)
            self.checkBox_normWHRatio.setChecked(False)
            self.checkBox_invertPatch.setChecked(False)
            self.checkBox_ordinalIndicator.setChecked(False)
            self.comboBox_binarizationMethod.setCurrentIndex(0)
        else:
            item_obj.settings = normalize_settings_dict(
                item_obj.settings, info_for_box_name(item_obj.name)
            )
            self.label_selectedInfo.setText(f"{item_obj.name}")
            self.lineEdit_format.setText(item_obj.settings["format_regex"])
            self.comboBox_fieldType.setCurrentIndex(item_obj.settings["type"])
            self.checkBox_smoothing.setChecked(item_obj.settings["smoothing"])
            self.checkBox_skip_empty.setChecked(item_obj.settings["skip_empty"])
            self.horizontalSlider_conf_thresh.setValue(
                int(item_obj.settings["conf_thresh"] * 100)
            )
            self.checkBox_autocrop.setChecked(item_obj.settings["autocrop"])
            self.checkBox_skip_similar_image.setChecked(
                item_obj.settings["skip_similar_image"]
            )
            self.horizontalSlider_cleanup.setValue(
                int(item_obj.settings["cleanup_thresh"] * 100)
            )
            self.horizontalSlider_dilate.setValue(item_obj.settings["dilate"])
            self.horizontalSlider_skew.setValue(item_obj.settings["skew"])
            self.horizontalSlider_vscale.setValue(item_obj.settings["vscale"])
            self.checkBox_removeLeadingZeros.setChecked(
                item_obj.settings["remove_leading_zeros"]
            )
            self.checkBox_rescalePatch.setChecked(item_obj.settings["rescale_patch"])
            self.checkBox_normWHRatio.setChecked(
                item_obj.settings["normalize_wh_ratio"]
            )
            self.checkBox_invertPatch.setChecked(item_obj.settings["invert_patch"])
            self.checkBox_ordinalIndicator.setChecked(
                item_obj.settings["ordinal_indicator"]
            )
            self.comboBox_binarizationMethod.setCurrentIndex(
                item_obj.settings["binarization_method"]
            )

        self.comboBox_formatPrefix.setCurrentIndex(12)

        self.lineEdit_format.blockSignals(False)
        self.comboBox_fieldType.blockSignals(False)
        self.checkBox_smoothing.blockSignals(False)
        self.checkBox_skip_empty.blockSignals(False)
        self.horizontalSlider_conf_thresh.blockSignals(False)
        self.checkBox_autocrop.blockSignals(False)
        self.checkBox_skip_similar_image.blockSignals(False)
        self.horizontalSlider_cleanup.blockSignals(False)
        self.horizontalSlider_dilate.blockSignals(False)
        self.horizontalSlider_skew.blockSignals(False)
        self.horizontalSlider_vscale.blockSignals(False)
        self.checkBox_removeLeadingZeros.blockSignals(False)
        self.checkBox_rescalePatch.blockSignals(False)
        self.checkBox_normWHRatio.blockSignals(False)
        self.checkBox_invertPatch.blockSignals(False)
        self.checkBox_ordinalIndicator.blockSignals(False)
        self.comboBox_binarizationMethod.blockSignals(False)
        self.comboBox_formatPrefix.blockSignals(False)

    def listItemClicked(self, item):
        if item.data(Qt.ItemDataRole.UserRole) == "checked":
            # enable the remove box button and disable the make box button
            self.pushButton_removeBox.setEnabled(True)
            self.pushButton_makeBox.setEnabled(False)
            self.groupBox_target_settings.setEnabled(True)
            self.populateSettings(item.text())
        else:
            # enable the make box button and disable the remove box button
            self.pushButton_removeBox.setEnabled(False)
            self.pushButton_makeBox.setEnabled(True)
            self.groupBox_target_settings.setEnabled(False)
            self.populateSettings("")

    def openOBSConnectModal(self):
        # disable OBS options
        self.lineEdit_sceneName.setEnabled(False)
        self.checkBox_recreate.setEnabled(False)
        self.pushButton_createOBSScene.setEnabled(False)

        # load the ui from "connect_obs.ui"
        path_to_dat = path.abspath(path.join(path.dirname(__file__), "connect_obs.ui"))
        self.obs_connect_modal = loadUi(path_to_dat)
        # connect the "connect" button to a function
        self.obs_connect_modal.pushButton_connect.clicked.connect(self.connectObs)
        # load the saved data from scoresight.json
        obs_data = fetch_data("scoresight.json", "obs")
        if obs_data:
            self.obs_connect_modal.lineEdit_ip.setText(obs_data["ip"])
            self.obs_connect_modal.lineEdit_port.setText(obs_data["port"])
            self.obs_connect_modal.lineEdit_password.setText(obs_data["password"])
        # show the modal
        self.obs_connect_modal.show()
        # focus the connect button
        self.obs_connect_modal.pushButton_connect.setFocus()

    def connectObs(self):
        # open a websocket connection to OBS using obs_websocket.py
        # enable the save button in the modal if the connection is successful
        if self.obs_connect_modal is not None:
            self.obs_websocket_client = open_obs_websocket(
                {
                    "ip": self.obs_connect_modal.lineEdit_ip.text(),
                    "port": self.obs_connect_modal.lineEdit_port.text(),
                    "password": self.obs_connect_modal.lineEdit_password.text(),
                }
            )
        else:
            self.obs_websocket_client = open_obs_websocket(
                fetch_data("scoresight.json", "obs")
            )
        if not self.obs_websocket_client:
            # show error in label_error
            if self.obs_connect_modal:
                self.obs_connect_modal.label_error.setText("Cannot connect to OBS")
            return

        # connection was successful
        if self.obs_connect_modal:
            store_data(
                "scoresight.json",
                "obs",
                {
                    "ip": self.obs_connect_modal.lineEdit_ip.text(),
                    "port": self.obs_connect_modal.lineEdit_port.text(),
                    "password": self.obs_connect_modal.lineEdit_password.text(),
                },
            )
            self.obs_connect_modal.close()

        self.lineEdit_sceneName.setEnabled(True)
        self.checkBox_recreate.setEnabled(True)
        self.pushButton_createOBSScene.setEnabled(True)

        # set OBS status to connected in the status bar
        self.statusbar.showMessage("OBS: Connected")

    @pyqtSlot()
    def getSources(self):
        # enumerate all the cameras
        camera_sources = get_camera_info()
        self.update_sources.emit(camera_sources)

    @pyqtSlot(list)
    def updateSources(self, camera_sources: list[CameraInfo]):
        # populate the combobox with the sources
        self.comboBox_camera_source.clear()
        self.comboBox_camera_source.addItem("Select a source")
        for source in camera_sources:
            self.comboBox_camera_source.addItem(source.description, source)

        # add an option to use a file as input
        self.comboBox_camera_source.addItem("Open a Video File", "file")
        self.comboBox_camera_source.addItem("URL Source (HTTP, RTSP)", "url")
        self.comboBox_camera_source.addItem("Screen Capture", "screen_capture")
        self.comboBox_camera_source.setEnabled(True)
        self.comboBox_camera_source.currentIndexChanged.connect(self.sourceChanged)

        # enable the source view frame
        self.frame_source_view.setEnabled(True)

        selected_source_from_storage = fetch_data("scoresight.json", "source_selected")
        if type(selected_source_from_storage) == str:
            logger.info(
                "Source selected from storage: %s", selected_source_from_storage
            )
            # check if the source is a file path
            if path.exists(selected_source_from_storage):
                self.comboBox_camera_source.blockSignals(True)
                self.comboBox_camera_source.setCurrentText("Open a Video File")
                self.comboBox_camera_source.blockSignals(False)
                self.source_name = selected_source_from_storage
                self.sourceSelectionSucessful()
            else:
                # select the last selected source
                self.comboBox_camera_source.setCurrentText(selected_source_from_storage)

    def sourceChanged(self, index):
        # get the source name from the combobox
        self.source_name = self.comboBox_camera_source.currentText()
        self.groupBox_sb_info.setEnabled(False)
        self.tableWidget_boxes.setEnabled(False)
        self.pushButton_fourCorner.setEnabled(False)
        self.pushButton_binary.setEnabled(False)
        if self.source_name == "Select a source":
            if self.image_viewer:
                # remove the image viewer from the layout frame_for_source_view_label
                self.frame_for_source_view_label.layout().removeWidget(
                    self.image_viewer
                )
                self.image_viewer.close()
                self.image_viewer = None
            # add a label with mardown text
            label_select_source = QLabel("### Open a Camera or Load a File")
            label_select_source.setTextFormat(Qt.TextFormat.MarkdownText)
            label_select_source.setEnabled(False)
            label_select_source.setAlignment(Qt.AlignmentFlag.AlignCenter)
            clear_layout(self.frame_for_source_view_label.layout())
            self.frame_for_source_view_label.layout().addWidget(label_select_source)
            return
        if self.source_name == "Open a Video File":
            # open a file dialog to select a video file
            file, _ = QFileDialog.getOpenFileName(
                self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mov)"
            )
            if not file:
                return
            self.source_name = file
        if self.source_name == "URL Source (HTTP, RTSP)":
            # open a dialog to enter the url
            url_dialog = QDialog()
            loadUi(
                path.abspath(path.join(path.dirname(__file__), "url_source.ui")),
                url_dialog,
            )
            url_dialog.setWindowTitle("URL Source")
            # focus on url input
            url_dialog.lineEdit_url.setFocus()
            url_dialog.exec()  # wait for the dialog to close
            # check if the dialog was accepted
            if url_dialog.result() != QDialog.DialogCode.Accepted:
                return
            self.source_name = url_dialog.lineEdit_url.text()
            if self.source_name == "":
                return
        if self.source_name == "Screen Capture":
            # open a dialog to select the screen
            screen_dialog = QDialog()
            loadUi(
                path.abspath(path.join(path.dirname(__file__), "screen_capture.ui")),
                screen_dialog,
            )
            screen_dialog.setWindowTitle("Screen Capture Selection")
            # populate comboBox_window with the available windows
            screen_dialog.comboBox_window.clear()
            screen_dialog.comboBox_window.addItem("Capture the entire screen", -1)
            for window in ScreenCapture.list_windows():
                screen_dialog.comboBox_window.addItem(window[0], window[1])
            screen_dialog.exec()
            # check if the dialog was accepted
            if screen_dialog.result() != QDialog.DialogCode.Accepted:
                return
            # get the window ID from the comboBox_window
            window_id = screen_dialog.comboBox_window.currentData()
            self.source_name = window_id

        # store the source selection in scoresight.json
        store_data("scoresight.json", "source_selected", self.source_name)
        self.sourceSelectionSucessful()

    def itemSelected(self, item_name):
        # select the item in the tableWidget_boxes
        items = self.tableWidget_boxes.findItems(item_name, Qt.MatchFlag.MatchExactly)
        if len(items) == 0:
            return
        item = items[0]
        item.setSelected(True)
        self.tableWidget_boxes.setCurrentItem(item)
        self.listItemClicked(item)

    def fourCornersApplied(self, corners):
        # check the button
        self.pushButton_fourCorner.setChecked(True)

    def sourceSelectionSucessful(self):
        if self.comboBox_camera_source.currentData() is None:
            return
        if self.comboBox_camera_source.currentText() == "Select a source":
            return

        self.frame_source_view.setEnabled(False)

        if self.comboBox_camera_source.currentData() == "file":
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.FILE,
            )
        elif self.comboBox_camera_source.currentData() == "url":
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.URL,
            )
        elif self.comboBox_camera_source.currentData() == "screen_capture":
            camera_info = CameraInfo(
                self.source_name,
                self.source_name,
                self.source_name,
                CameraInfo.CameraType.SCREEN_CAPTURE,
            )
        else:
            camera_info = self.comboBox_camera_source.currentData()

        if self.image_viewer:
            # remove the image viewer from the layout frame_for_source_view_label
            self.frame_for_source_view_label.layout().removeWidget(self.image_viewer)
            self.image_viewer.close()
            self.image_viewer = None

        # clear self.frame_for_source_view_label
        clear_layout(self.frame_for_source_view_label.layout())

        # set the pixmap to the image viewer
        self.image_viewer = ImageViewer(
            camera_info,
            self.fourCornersApplied,
            self.detectionTargetsStorage,
            self.itemSelected,
        )
        self.pushButton_fourCorner.setEnabled(True)
        self.pushButton_binary.setEnabled(True)
        self.pushButton_fourCorner.toggled.connect(self.image_viewer.toggleFourCorner)
        self.pushButton_binary.clicked.connect(self.image_viewer.toggleBinary)
        if self.image_viewer.timerThread:
            self.image_viewer.timerThread.ocr_result_signal.connect(self.ocrResult)
            self.image_viewer.timerThread.update_error.connect(self.updateError)
        self.image_viewer.first_frame_received_signal.connect(
            self.cameraConnectedEnableUI
        )
        self.ocrModelChanged(fetch_data("scoresight.json", "ocr_model", 1))

        # set the image viewer to the layout frame_for_source_view_label
        self.frame_for_source_view_label.layout().addWidget(self.image_viewer)

    def cameraConnectedEnableUI(self):
        # enable groupBox_sb_info
        self.groupBox_sb_info.setEnabled(True)
        self.tableWidget_boxes.setEnabled(True)
        self.frame_source_view.setEnabled(True)
        self.widget_viewTools.setEnabled(True)

        # load the boxes from scoresight.json
        self.detectionTargetsStorage.loadBoxesFromStorage()
        self.updateError(None)

    def updateError(self, error):
        if not error:
            self.statusbar.clearMessage()
            return
        # show the error in the status bar
        self.statusbar.showMessage(error)
        self.frame_source_view.setEnabled(True)
        self.widget_viewTools.setEnabled(False)

    def ocrResult(self, results: list[TextDetectionTargetWithResult]):
        if not self.updateOCRResults:
            # don't update the results, the user has disabled updates
            return

        update_http_server(results)

        # update vmix
        self.vmixUpdater.update_vmix(results)

        # update the table widget value items
        for targetWithResult in results:
            if (
                targetWithResult.result_state
                == TextDetectionTargetWithResult.ResultState.Success
            ):
                items = self.tableWidget_boxes.findItems(
                    targetWithResult.name, Qt.MatchFlag.MatchExactly
                )
                if len(items) == 0:
                    continue
                item = items[0]
                # get the value (1 column) of the item
                item = self.tableWidget_boxes.item(item.row(), 1)
                item.setText(targetWithResult.result)

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
        ).total_seconds() < 1.0 / self.horizontalSlider_aggsPerSecond.value():
            return

        self.last_aggregate_save = datetime.datetime.now()

        # update the obs scene sources with the results, use update_text_source
        for targetWithResult in results:
            if targetWithResult.result is None:
                continue
            if (
                "skip_empty" in targetWithResult.settings
                and targetWithResult.settings["skip_empty"]
                and len(targetWithResult.result) == 0
            ):
                continue
            if (
                targetWithResult.result_state
                != TextDetectionTargetWithResult.ResultState.Success
            ):
                continue

            if self.obs_websocket_client is not None:
                # find the source name for the target from the default boxes
                update_text_source(
                    self.obs_websocket_client,
                    targetWithResult.settings["obs_source_name"],
                    targetWithResult.result,
                )

        # save the results to text files
        file_output.save_text_files(
            results, self.out_folder, self.comboBox_appendMethod.currentIndex()
        )

        # save the results to a csv file
        if self.checkBox_saveCsv.isChecked():
            file_output.save_csv(
                results,
                self.out_folder,
                self.comboBox_appendMethod.currentIndex(),
                self.first_csv_append,
            )

        # save the results to an xml file
        if self.checkBox_saveXML.isChecked():
            file_output.save_xml(
                results,
                self.out_folder,
            )

    def addBox(self):
        # add a new box to the tableWidget_boxes
        # find the number of custom boxes
        custom_boxes = []
        for i in range(self.tableWidget_boxes.rowCount()):
            item = self.tableWidget_boxes.item(i, 0)
            if item.text() not in [o["name"] for o in default_boxes]:
                custom_boxes.append(item.text())

        store_custom_box_name("Custom")
        item = QTableWidgetItem(
            QIcon(
                path.abspath(path.join(path.dirname(__file__), "icons/circle-x.svg"))
            ),
            "Custom",
        )
        item.setData(Qt.ItemDataRole.UserRole, "unchecked")
        self.tableWidget_boxes.insertRow(self.tableWidget_boxes.rowCount())
        self.tableWidget_boxes.setItem(self.tableWidget_boxes.rowCount() - 1, 0, item)
        disabledItem = QTableWidgetItem()
        disabledItem.setFlags(Qt.ItemFlag.NoItemFlags)
        self.tableWidget_boxes.setItem(
            self.tableWidget_boxes.rowCount() - 1, 1, disabledItem
        )

    def removeCustomBox(self):
        item = self.tableWidget_boxes.currentItem()
        if not item:
            logger.info("No item selected")
            return
        if item.column() != 0:
            item = self.tableWidget_boxes.item(item.row(), 0)
        self.removeBox()
        remove_custom_box_name_in_storage(item.text())
        # only allow removing custom boxes
        if item.text() in [o["name"] for o in default_boxes]:
            logger.info("Cannot remove default box")
            return
        # remove the selected item from the tableWidget_boxes
        self.tableWidget_boxes.removeRow(item.row())

    def editBoxName(self, item):
        if item.text() in [o["name"] for o in default_boxes]:
            return
        new_name, ok = QInputDialog.getText(
            self, "Edit Box Name", "New Name:", text=item.text()
        )
        if ok and new_name != "" and new_name != item.text():
            # check if name doesn't exist already
            for i in range(self.tableWidget_boxes.rowCount()):
                if new_name == self.tableWidget_boxes.item(i, 0).text():
                    logger.info("Name '%s' already exists", new_name)
                    return
            # rename the item in the detectionTargetsStorage
            if not self.detectionTargetsStorage.rename_item(item.text(), new_name):
                logger.info("Error renaming item in application storage")
                return
            # rename the item in the tableWidget_boxes
            item.setText(new_name)
            rename_custom_box_name_in_storage(item.text(), new_name)

    def makeBox(self):
        item = self.tableWidget_boxes.currentItem()
        if not item:
            return
        # create a new box on self.image_viewer with the name of the selected item from the tableWidget_boxes
        # change the list icon to green checkmark
        item.setIcon(
            QIcon(
                path.abspath(
                    path.join(path.dirname(__file__), "icons/circle-check.svg")
                )
            )
        )
        item.setData(Qt.ItemDataRole.UserRole, "checked")
        self.listItemClicked(item)

        # get the size of the box from the name
        info = info_for_box_name(item.text())

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
        item = self.tableWidget_boxes.currentItem()
        if not item:
            return
        # change the list icon to red x
        item.setIcon(
            QIcon(path.abspath(path.join(path.dirname(__file__), "icons/circle-x.svg")))
        )
        item.setData(Qt.ItemDataRole.UserRole, "unchecked")
        self.listItemClicked(item)
        self.detectionTargetsStorage.remove_item(item.text())

    def createOBSScene(self):
        self.statusBar().showMessage("Creating OBS scene")
        # get the scene name from the lineEdit_sceneName
        scene_name = self.lineEdit_sceneName.text()
        # clear or create a new scene
        create_obs_scene_from_export(self.obs_websocket_client, scene_name)
        self.statusBar().showMessage("Finished creating scene")

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


if __name__ == "__main__":
    # only attempt splash when not on Mac OSX
    os_name = platform.system()
    if os_name != "Darwin":
        try:
            import pyi_splash

            pyi_splash.close()
        except ImportError:
            pass
    app = QApplication(sys.argv)

    # show the main window
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()
    logger.info("Exiting...")

    stop_http_server()
