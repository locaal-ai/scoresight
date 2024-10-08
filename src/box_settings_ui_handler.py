from functools import partial

from defaults import (
    default_info_for_box_name,
    normalize_settings_dict,
    format_prefixes,
)
from storage import TextDetectionTargetMemoryStorage
from ui_mainwindow import Ui_MainWindow
from sc_logging import logger


class BoxSettingsUIHandler:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.boxSettingsUiSetup()
        self.detectionTargetsStorage = TextDetectionTargetMemoryStorage()

    def editSettings(self, settingsMutatorCallback):
        # update the selected item's settings in the detectionTargetsStorage
        item = self.ui.tableWidget_boxes.currentItem()
        if item is None:
            logger.info("no item selected")
            return
        item_name = item.text()
        item_obj = self.detectionTargetsStorage.find_item_by_name(item_name)
        if item_obj is None:
            logger.info("item not found: %s", item_name)
            return
        item_obj = settingsMutatorCallback(item_obj)
        self.detectionTargetsStorage.edit_item(item_name, item_obj)

    def restoreDefaults(self):
        # restore the default settings for the selected item
        def restoreDefaultsSettings(item_obj):
            info = default_info_for_box_name(item_obj.name)
            item_obj.settings = normalize_settings_dict({}, info)
            return item_obj

        self.editSettings(restoreDefaultsSettings)
        self.populateSettings(self.ui.tableWidget_boxes.currentItem().text())

    def confThreshChanged(self):
        self.genericSettingsChanged(
            "conf_thresh", float(self.ui.horizontalSlider_conf_thresh.value()) / 100.0
        )

    def cleanupThreshChanged(self):
        self.genericSettingsChanged(
            "cleanup_thresh", float(self.ui.horizontalSlider_cleanup.value()) / 100.0
        )

    def formatPrefixChanged(self, index):
        if index == 12:
            return  # do nothing if "Select Preset" is selected
        # based on the selected index, set the format prefix
        # change lineEdit_format to the selected format prefix
        self.ui.lineEdit_format.setText(format_prefixes[index])

    def genericSettingsChanged(self, settingName, value):
        def editGenericSettings(item_obj):
            item_obj.settings[settingName] = value
            return item_obj

        self.editSettings(editGenericSettings)

    def boxSettingsUiSetup(self):
        self.ui.pushButton_restoreDefaults.clicked.connect(self.restoreDefaults)
        self.ui.checkBox_smoothing.toggled.connect(
            partial(self.genericSettingsChanged, "smoothing")
        )
        self.ui.checkBox_skip_empty.toggled.connect(
            partial(self.genericSettingsChanged, "skip_empty")
        )
        self.ui.horizontalSlider_conf_thresh.valueChanged.connect(
            self.confThreshChanged
        )
        self.ui.lineEdit_format.textChanged.connect(
            partial(self.genericSettingsChanged, "format_regex")
        )
        self.ui.comboBox_fieldType.currentIndexChanged.connect(
            partial(self.genericSettingsChanged, "type")
        )
        self.ui.checkBox_skip_similar_image.toggled.connect(
            partial(self.genericSettingsChanged, "skip_similar_image")
        )
        self.ui.checkBox_autocrop.toggled.connect(
            partial(self.genericSettingsChanged, "autocrop")
        )
        self.ui.horizontalSlider_cleanup.valueChanged.connect(self.cleanupThreshChanged)
        self.ui.horizontalSlider_dilate.valueChanged.connect(
            partial(self.genericSettingsChanged, "dilate")
        )
        self.ui.horizontalSlider_skew.valueChanged.connect(
            partial(self.genericSettingsChanged, "skew")
        )
        self.ui.horizontalSlider_vscale.valueChanged.connect(
            partial(self.genericSettingsChanged, "vscale")
        )
        self.ui.checkBox_removeLeadingZeros.toggled.connect(
            partial(self.genericSettingsChanged, "remove_leading_zeros")
        )
        self.ui.checkBox_rescalePatch.toggled.connect(
            partial(self.genericSettingsChanged, "rescale_patch")
        )
        self.ui.checkBox_normWHRatio.toggled.connect(
            partial(self.genericSettingsChanged, "normalize_wh_ratio")
        )
        self.ui.checkBox_invertPatch.toggled.connect(
            partial(self.genericSettingsChanged, "invert_patch")
        )
        self.ui.checkBox_dotDetector.toggled.connect(
            partial(self.genericSettingsChanged, "dot_detector")
        )
        self.ui.checkBox_ordinalIndicator.toggled.connect(
            partial(self.genericSettingsChanged, "ordinal_indicator")
        )
        self.ui.comboBox_binarizationMethod.currentIndexChanged.connect(
            partial(self.genericSettingsChanged, "binarization_method")
        )
        self.ui.lineEdit_templatefield.textChanged.connect(
            partial(self.genericSettingsChanged, "templatefield_text")
        )
        self.ui.checkBox_compositeBox.toggled.connect(
            partial(self.genericSettingsChanged, "composite_box")
        )
        self.ui.comboBox_formatPrefix.currentIndexChanged.connect(
            self.formatPrefixChanged
        )

    def populateSettings(self, name):
        self.ui.lineEdit_format.blockSignals(True)
        self.ui.comboBox_fieldType.blockSignals(True)
        self.ui.checkBox_smoothing.blockSignals(True)
        self.ui.checkBox_skip_empty.blockSignals(True)
        self.ui.horizontalSlider_conf_thresh.blockSignals(True)
        self.ui.checkBox_autocrop.blockSignals(True)
        self.ui.checkBox_skip_similar_image.blockSignals(True)
        self.ui.horizontalSlider_cleanup.blockSignals(True)
        self.ui.horizontalSlider_dilate.blockSignals(True)
        self.ui.horizontalSlider_skew.blockSignals(True)
        self.ui.horizontalSlider_vscale.blockSignals(True)
        self.ui.checkBox_removeLeadingZeros.blockSignals(True)
        self.ui.checkBox_rescalePatch.blockSignals(True)
        self.ui.checkBox_normWHRatio.blockSignals(True)
        self.ui.checkBox_invertPatch.blockSignals(True)
        self.ui.checkBox_ordinalIndicator.blockSignals(True)
        self.ui.comboBox_binarizationMethod.blockSignals(True)
        self.ui.comboBox_formatPrefix.blockSignals(True)
        self.ui.checkBox_templatefield.blockSignals(True)
        self.ui.lineEdit_templatefield.blockSignals(True)
        self.ui.checkBox_compositeBox.blockSignals(True)

        # populate the settings from the detectionTargetsStorage
        item_obj = self.detectionTargetsStorage.find_item_by_name(name)
        if item_obj is None:
            self.ui.lineEdit_format.setText("")
            self.ui.comboBox_fieldType.setCurrentIndex(0)
            self.ui.checkBox_smoothing.setChecked(True)
            self.ui.checkBox_skip_empty.setChecked(True)
            self.ui.horizontalSlider_conf_thresh.setValue(50)
            self.ui.checkBox_autocrop.setChecked(False)
            self.ui.checkBox_skip_similar_image.setChecked(False)
            self.ui.horizontalSlider_cleanup.setValue(0)
            self.ui.horizontalSlider_dilate.setValue(1)
            self.ui.horizontalSlider_skew.setValue(0)
            self.ui.horizontalSlider_vscale.setValue(10)
            self.ui.label_selectedInfo.setText("")
            self.ui.checkBox_removeLeadingZeros.setChecked(False)
            self.ui.checkBox_rescalePatch.setChecked(False)
            self.ui.checkBox_normWHRatio.setChecked(False)
            self.ui.checkBox_invertPatch.setChecked(False)
            self.ui.checkBox_ordinalIndicator.setChecked(False)
            self.ui.comboBox_binarizationMethod.setCurrentIndex(0)
            self.ui.checkBox_templatefield.setChecked(False)
            self.ui.lineEdit_templatefield.setText("")
            self.ui.checkBox_compositeBox.setChecked(False)
        else:
            item_obj.settings = normalize_settings_dict(
                item_obj.settings, default_info_for_box_name(item_obj.name)
            )
            self.ui.label_selectedInfo.setText(f"{item_obj.name}")
            self.ui.lineEdit_format.setText(item_obj.settings["format_regex"])
            self.ui.comboBox_fieldType.setCurrentIndex(item_obj.settings["type"])
            self.ui.checkBox_smoothing.setChecked(item_obj.settings["smoothing"])
            self.ui.checkBox_skip_empty.setChecked(item_obj.settings["skip_empty"])
            self.ui.horizontalSlider_conf_thresh.setValue(
                int(item_obj.settings["conf_thresh"] * 100)
            )
            self.ui.checkBox_autocrop.setChecked(item_obj.settings["autocrop"])
            self.ui.checkBox_skip_similar_image.setChecked(
                item_obj.settings["skip_similar_image"]
            )
            self.ui.horizontalSlider_cleanup.setValue(
                int(item_obj.settings["cleanup_thresh"] * 100)
            )
            self.ui.horizontalSlider_dilate.setValue(item_obj.settings["dilate"])
            self.ui.horizontalSlider_skew.setValue(item_obj.settings["skew"])
            self.ui.horizontalSlider_vscale.setValue(item_obj.settings["vscale"])
            self.ui.checkBox_removeLeadingZeros.setChecked(
                item_obj.settings["remove_leading_zeros"]
            )
            self.ui.checkBox_rescalePatch.setChecked(item_obj.settings["rescale_patch"])
            self.ui.checkBox_normWHRatio.setChecked(
                item_obj.settings["normalize_wh_ratio"]
            )
            self.ui.checkBox_invertPatch.setChecked(item_obj.settings["invert_patch"])
            self.ui.checkBox_dotDetector.setChecked(item_obj.settings["dot_detector"])
            self.ui.checkBox_ordinalIndicator.setChecked(
                item_obj.settings["ordinal_indicator"]
            )
            self.ui.comboBox_binarizationMethod.setCurrentIndex(
                item_obj.settings["binarization_method"]
            )
            self.ui.checkBox_templatefield.setChecked(
                item_obj.settings["templatefield"]
            )
            self.ui.lineEdit_templatefield.setText(
                item_obj.settings["templatefield_text"]
            )
            self.ui.checkBox_compositeBox.setChecked(item_obj.settings["composite_box"])

        self.ui.comboBox_formatPrefix.setCurrentIndex(12)

        self.ui.lineEdit_format.blockSignals(False)
        self.ui.comboBox_fieldType.blockSignals(False)
        self.ui.checkBox_smoothing.blockSignals(False)
        self.ui.checkBox_skip_empty.blockSignals(False)
        self.ui.horizontalSlider_conf_thresh.blockSignals(False)
        self.ui.checkBox_autocrop.blockSignals(False)
        self.ui.checkBox_skip_similar_image.blockSignals(False)
        self.ui.horizontalSlider_cleanup.blockSignals(False)
        self.ui.horizontalSlider_dilate.blockSignals(False)
        self.ui.horizontalSlider_skew.blockSignals(False)
        self.ui.horizontalSlider_vscale.blockSignals(False)
        self.ui.checkBox_removeLeadingZeros.blockSignals(False)
        self.ui.checkBox_rescalePatch.blockSignals(False)
        self.ui.checkBox_normWHRatio.blockSignals(False)
        self.ui.checkBox_invertPatch.blockSignals(False)
        self.ui.checkBox_ordinalIndicator.blockSignals(False)
        self.ui.comboBox_binarizationMethod.blockSignals(False)
        self.ui.comboBox_formatPrefix.blockSignals(False)
        self.ui.checkBox_templatefield.blockSignals(False)
        self.ui.lineEdit_templatefield.blockSignals(False)
        self.ui.checkBox_compositeBox.blockSignals(False)
