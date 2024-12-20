# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 259)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBox_fourcc = QComboBox(self.widget)
        self.comboBox_fourcc.addItem("")
        self.comboBox_fourcc.setObjectName(u"comboBox_fourcc")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_fourcc)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.spinBox_fps = QSpinBox(self.widget)
        self.spinBox_fps.setObjectName(u"spinBox_fps")
        self.spinBox_fps.setMinimum(1)
        self.spinBox_fps.setMaximum(60)
        self.spinBox_fps.setValue(30)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBox_fps)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.comboBox_resolution = QComboBox(self.widget)
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.setObjectName(u"comboBox_resolution")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_resolution)

        self.plainTextEdit_videoProps = QPlainTextEdit(self.widget)
        self.plainTextEdit_videoProps.setObjectName(u"plainTextEdit_videoProps")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.plainTextEdit_videoProps)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.comboBox_captureBackend = QComboBox(self.widget)
        self.comboBox_captureBackend.addItem("")
        self.comboBox_captureBackend.setObjectName(u"comboBox_captureBackend")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_captureBackend)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Video Format", None))
        self.comboBox_fourcc.setItemText(0, QCoreApplication.translate("Dialog", u"Default", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"FPS", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Resolution", None))
        self.comboBox_resolution.setItemText(0, QCoreApplication.translate("Dialog", u"Default", None))
        self.comboBox_resolution.setItemText(1, QCoreApplication.translate("Dialog", u"320x240", None))
        self.comboBox_resolution.setItemText(2, QCoreApplication.translate("Dialog", u"640x480", None))
        self.comboBox_resolution.setItemText(3, QCoreApplication.translate("Dialog", u"800x600", None))
        self.comboBox_resolution.setItemText(4, QCoreApplication.translate("Dialog", u"1280x720", None))
        self.comboBox_resolution.setItemText(5, QCoreApplication.translate("Dialog", u"1280x960", None))
        self.comboBox_resolution.setItemText(6, QCoreApplication.translate("Dialog", u"1600x900", None))
        self.comboBox_resolution.setItemText(7, QCoreApplication.translate("Dialog", u"1980x1080", None))
        self.comboBox_resolution.setItemText(8, QCoreApplication.translate("Dialog", u"3840x2160", None))
        self.comboBox_resolution.setItemText(9, QCoreApplication.translate("Dialog", u"2560x1440", None))
        self.comboBox_resolution.setItemText(10, QCoreApplication.translate("Dialog", u"2048x1080", None))
        self.comboBox_resolution.setItemText(11, QCoreApplication.translate("Dialog", u"4096x2160", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Capture Backend", None))
        self.comboBox_captureBackend.setItemText(0, QCoreApplication.translate("Dialog", u"Default / Any", None))

    # retranslateUi

