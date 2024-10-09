from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from text_detection_target import TextDetectionTarget
from ui_mainwindow import Ui_MainWindow
from vmix_output import VMixAPI
from sc_logging import logger
from storage import fetch_data, store_data


class VMixUIHanlder:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.vmixUpdater = None
        self.vmixUiSetup()

    def globalSettingsChanged(self, settingName, value):
        store_data("scoresight.json", settingName, value)

    def vmixConnectionChanged(self):
        self.vmixUpdater = VMixAPI(
            self.ui.lineEdit_vmixHost.text(),
            self.ui.lineEdit_vmixPort.text(),
            self.ui.inputLineEdit_vmix.text(),
            {},
        )
        self.globalSettingsChanged("vmix_host", self.ui.lineEdit_vmixHost.text())
        self.globalSettingsChanged("vmix_port", self.ui.lineEdit_vmixPort.text())
        self.globalSettingsChanged("vmix_input", self.ui.inputLineEdit_vmix.text())

    def vmixMappingChanged(self, _):
        # store entire mapping data in scoresight.json
        mapping = {}
        model = self.ui.tableView_vmixMapping.model()
        if isinstance(model, QStandardItemModel):
            for i in range(model.rowCount()):
                item = model.item(i, 0)
                value = model.item(i, 1)
                if item and value:
                    mapping[item.text()] = value.text()
            self.globalSettingsChanged("vmix_mapping", mapping)
            self.vmixUpdater.set_field_mapping(mapping)
        else:
            logger.error("vmixMappingChanged: model is not a QStandardItemModel")

    def vmixUiSetup(self):
        # populate the vmix connection from storage
        self.ui.lineEdit_vmixHost.setText(
            fetch_data("scoresight.json", "vmix_host", "localhost")
        )
        self.ui.lineEdit_vmixPort.setText(
            fetch_data("scoresight.json", "vmix_port", "8099")
        )
        self.ui.inputLineEdit_vmix.setText(
            fetch_data("scoresight.json", "vmix_input", "1")
        )
        # connect the lineEdits to vmixConnectionChanged
        self.ui.lineEdit_vmixHost.textChanged.connect(self.vmixConnectionChanged)
        self.ui.lineEdit_vmixPort.textChanged.connect(self.vmixConnectionChanged)
        self.ui.inputLineEdit_vmix.textChanged.connect(self.vmixConnectionChanged)

        # create the vmixUpdater
        self.vmixUpdater = VMixAPI(
            self.ui.lineEdit_vmixHost.text(),
            self.ui.lineEdit_vmixPort.text(),
            self.ui.inputLineEdit_vmix.text(),
            {},
        )
        # add standard item model to the tableView_vmixMapping
        self.ui.tableView_vmixMapping.setModel(QStandardItemModel())
        mapping = fetch_data("scoresight.json", "vmix_mapping", {})
        if mapping:
            self.vmixUpdater.set_field_mapping(mapping)

        self.ui.tableView_vmixMapping.model().dataChanged.connect(
            self.vmixMappingChanged
        )

        self.ui.pushButton_startvmix.toggled.connect(self.togglevMix)

    def togglevMix(self, value):
        if not self.vmixUpdater:
            return
        if value:
            self.ui.pushButton_startvmix.setText("🛑 Stop vMix")
            self.vmixUpdater.running = True
        else:
            self.ui.pushButton_startvmix.setText("▶️ Start vMix")
            self.vmixUpdater.running = False

    def updatevMixTable(self, detectionTargets: list[TextDetectionTarget]):
        mapping_storage = fetch_data("scoresight.json", "vmix_mapping")
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
            else:
                # update the item in the list
                item = items[0]
                row = item.row()

            # get value from storage or use the box name
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
        self.ui.tableView_vmixMapping.setModel(model)
        self.ui.tableView_vmixMapping.model().dataChanged.connect(
            self.vmixMappingChanged
        )
