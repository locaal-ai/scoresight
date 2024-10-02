# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ocr_training_data_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QWidget)

class Ui_OCRTrainingDataDialog(object):
    def setupUi(self, OCRTrainingDataDialog):
        if not OCRTrainingDataDialog.objectName():
            OCRTrainingDataDialog.setObjectName(u"OCRTrainingDataDialog")
        OCRTrainingDataDialog.resize(377, 164)
        OCRTrainingDataDialog.setMinimumSize(QSize(267, 0))
        OCRTrainingDataDialog.setMaximumSize(QSize(650, 300))
        self.gridLayout = QGridLayout(OCRTrainingDataDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(OCRTrainingDataDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_saveFolder = QLineEdit(self.widget_2)
        self.lineEdit_saveFolder.setObjectName(u"lineEdit_saveFolder")

        self.horizontalLayout.addWidget(self.lineEdit_saveFolder)

        self.toolButton_chooseSaveFolder = QToolButton(self.widget_2)
        self.toolButton_chooseSaveFolder.setObjectName(u"toolButton_chooseSaveFolder")

        self.horizontalLayout.addWidget(self.toolButton_chooseSaveFolder)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_openFolder = QPushButton(self.widget_3)
        self.pushButton_openFolder.setObjectName(u"pushButton_openFolder")

        self.horizontalLayout_2.addWidget(self.pushButton_openFolder)

        self.pushButton_saveZipFile = QPushButton(self.widget_3)
        self.pushButton_saveZipFile.setObjectName(u"pushButton_saveZipFile")

        self.horizontalLayout_2.addWidget(self.pushButton_saveZipFile)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widget_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.spinBox_maxSize = QSpinBox(self.widget)
        self.spinBox_maxSize.setObjectName(u"spinBox_maxSize")
        self.spinBox_maxSize.setMinimum(1)
        self.spinBox_maxSize.setValue(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_maxSize)

        self.pushButton_openTrainingDojo = QPushButton(self.widget)
        self.pushButton_openTrainingDojo.setObjectName(u"pushButton_openTrainingDojo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_openTrainingDojo)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(OCRTrainingDataDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(OCRTrainingDataDialog)
        self.buttonBox.accepted.connect(OCRTrainingDataDialog.accept)
        self.buttonBox.rejected.connect(OCRTrainingDataDialog.reject)

        QMetaObject.connectSlotsByName(OCRTrainingDataDialog)
    # setupUi

    def retranslateUi(self, OCRTrainingDataDialog):
        OCRTrainingDataDialog.setWindowTitle(QCoreApplication.translate("OCRTrainingDataDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"Save Folder", None))
        self.toolButton_chooseSaveFolder.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"...", None))
        self.pushButton_openFolder.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"Open Folder", None))
        self.pushButton_saveZipFile.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"Save Zip File", None))
        self.label_2.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"Max Size", None))
        self.spinBox_maxSize.setSuffix(QCoreApplication.translate("OCRTrainingDataDialog", u"Mb", None))
        self.pushButton_openTrainingDojo.setText(QCoreApplication.translate("OCRTrainingDataDialog", u"Open OCR Training Dojo", None))
    # retranslateUi

