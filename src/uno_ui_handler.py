from functools import partial
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from text_detection_target import TextDetectionTarget
from ui_mainwindow import Ui_MainWindow
from uno_output import UNOAPI
from sc_logging import logger
from storage import fetch_data, store_data

standard_uno_mapping = {
    "Time": "SetMatchTime",
    "Home Score": "SetGoalsHome",
    "Away Score": "SetGoalsAway",
    "Period": "SetPeriod",
}


class UNOUIHandler:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.unoUpdater = None
        self.unoUiSetup()

    def globalSettingsChanged(self, settingName, value):
        store_data("scoresight.json", settingName, value)

    def unoConnectionChanged(self):
        self.unoUpdater = UNOAPI(
            self.ui.lineEdit_unoUrl.text(),
            {},
        )
        self.globalSettingsChanged("uno_url", self.ui.lineEdit_unoUrl.text())
        self.unoMappingChanged(True)

    def unoMappingChanged(self, shouldUpdateStorage: bool):
        mapping = {}
        model = self.ui.tableView_unoMapping.model()
        if isinstance(model, QStandardItemModel):
            for i in range(model.rowCount()):
                item = model.item(i, 0)
                value = model.item(i, 1)
                if item and value:
                    mapping[item.text()] = value.text()
            if shouldUpdateStorage:
                self.globalSettingsChanged("uno_mapping", mapping)
            self.unoUpdater.set_field_mapping(mapping)
        else:
            logger.error("unoMappingChanged: model is not a QStandardItemModel")

    def unoUiSetup(self):
        # populate the UNO connection from storage
        self.ui.lineEdit_unoUrl.setText(
            fetch_data(
                "scoresight.json",
                "uno_url",
                "https://app.overlays.uno/apiv2/controlapps/.../api",
            )
        )
        # connect the lineEdit to unoConnectionChanged
        self.ui.lineEdit_unoUrl.textChanged.connect(self.unoConnectionChanged)

        # create the unoUpdater
        self.unoUpdater = UNOAPI(
            self.ui.lineEdit_unoUrl.text(),
            {},
        )
        # add standard item model to the tableView_unoMapping
        self.ui.tableView_unoMapping.setModel(QStandardItemModel())
        mapping = fetch_data("scoresight.json", "uno_mapping", {})
        if mapping:
            self.unoUpdater.set_field_mapping(mapping)

        self.ui.tableView_unoMapping.model().dataChanged.connect(self.unoMappingChanged)

        self.ui.toolButton_toggleUno.toggled.connect(self.toggleUNO)

        # Connect the "Send Same?" checkbox
        self.ui.checkBox_uno_send_same.setChecked(
            fetch_data("scoresight.json", "uno_send_same", False)
        )
        self.ui.checkBox_uno_send_same.stateChanged.connect(
            partial(self.globalSettingsChanged, "uno_send_same")
        )

        # connect the "essentials" checkbox
        self.ui.checkBox_uno_essentials.setChecked(
            fetch_data("scoresight.json", "uno_essentials", False)
        )
        self.ui.checkBox_uno_essentials.stateChanged.connect(self.set_uno_essentials)
        # show/ hide widget_uno_essentials_details based on the checkbox
        self.ui.widget_uno_essentials_details.setVisible(
            self.ui.checkBox_uno_essentials.isChecked()
        )

        # connect lineEdit_uno_essentials_id
        self.ui.lineEdit_uno_essentials_id.setText(
            fetch_data("scoresight.json", "uno_essentials_id", "")
        )
        self.ui.lineEdit_uno_essentials_id.textChanged.connect(
            partial(self.globalSettingsChanged, "uno_essentials_id")
        )

    def set_uno_essentials(self, value):
        self.globalSettingsChanged("uno_essentials", value)
        self.ui.widget_uno_essentials_details.setVisible(value)

    def toggleUNO(self, value):
        if not self.unoUpdater:
            return
        if value:
            self.ui.toolButton_toggleUno.setText("🛑")
            self.unoUpdater.start()
        else:
            self.ui.toolButton_toggleUno.setText("▶️")
            self.unoUpdater.stop()

    def updateUNOTable(self, detectionTargets: list[TextDetectionTarget]):
        mapping_storage = fetch_data("scoresight.json", "uno_mapping")
        model = QStandardItemModel()
        model.blockSignals(True)

        for box in detectionTargets:
            items = model.findItems(box.name, Qt.MatchFlag.MatchExactly)
            if len(items) == 0:
                row = model.rowCount()
                model.insertRow(row)
                model.setItem(row, 0, QStandardItem(box.name))
                model.item(row, 0).setFlags(Qt.ItemFlag.ItemIsEnabled)
            else:
                item = items[0]
                row = item.row()

            new_item_value = None
            if mapping_storage and box.name in mapping_storage:
                new_item_value = mapping_storage[box.name]
            else:
                if box.name in standard_uno_mapping:
                    new_item_value = standard_uno_mapping[box.name]
                else:
                    new_item_value = box.name
            model.setItem(row, 1, QStandardItem(new_item_value))

        for i in range(model.rowCount() - 1, -1, -1):
            item = model.item(i, 0)
            if not any([box.name == item.text() for box in detectionTargets]):
                model.removeRow(i)

        model.blockSignals(False)
        self.ui.tableView_unoMapping.setModel(model)
        self.ui.tableView_unoMapping.model().dataChanged.connect(self.unoMappingChanged)
        self.unoMappingChanged(False)
