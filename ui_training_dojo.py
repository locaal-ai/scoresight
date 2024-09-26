# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'training_dojo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TrainingDojo(object):
    def setupUi(self, TrainingDojo):
        if not TrainingDojo.objectName():
            TrainingDojo.setObjectName(u"TrainingDojo")
        TrainingDojo.resize(658, 446)
        TrainingDojo.setMaximumSize(QSize(660, 450))
        self.gridLayout = QGridLayout(TrainingDojo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_files = QListWidget(TrainingDojo)
        self.listWidget_files.setObjectName(u"listWidget_files")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_files.sizePolicy().hasHeightForWidth())
        self.listWidget_files.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.listWidget_files, 1, 0, 1, 1)

        self.widget = QWidget(TrainingDojo)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_image = QWidget(self.widget)
        self.widget_image.setObjectName(u"widget_image")
        self.gridLayout_2 = QGridLayout(self.widget_image)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_imagePlaceholder = QLabel(self.widget_image)
        self.label_imagePlaceholder.setObjectName(u"label_imagePlaceholder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_imagePlaceholder.sizePolicy().hasHeightForWidth())
        self.label_imagePlaceholder.setSizePolicy(sizePolicy2)
        self.label_imagePlaceholder.setScaledContents(True)
        self.label_imagePlaceholder.setAlignment(Qt.AlignCenter)
        self.label_imagePlaceholder.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_imagePlaceholder, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_image)

        self.lineEdit_text = QLineEdit(self.widget)
        self.lineEdit_text.setObjectName(u"lineEdit_text")
        font = QFont()
        font.setPointSize(29)
        self.lineEdit_text.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_text)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_prev = QPushButton(self.widget_3)
        self.pushButton_prev.setObjectName(u"pushButton_prev")

        self.horizontalLayout.addWidget(self.pushButton_prev)

        self.pushButton_next = QPushButton(self.widget_3)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout.addWidget(self.pushButton_next)


        self.verticalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)

        self.pushButton_onlyUndone = QPushButton(TrainingDojo)
        self.pushButton_onlyUndone.setObjectName(u"pushButton_onlyUndone")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_onlyUndone.sizePolicy().hasHeightForWidth())
        self.pushButton_onlyUndone.setSizePolicy(sizePolicy4)
        self.pushButton_onlyUndone.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_onlyUndone, 2, 0, 1, 1)


        self.retranslateUi(TrainingDojo)

        QMetaObject.connectSlotsByName(TrainingDojo)
    # setupUi

    def retranslateUi(self, TrainingDojo):
        TrainingDojo.setWindowTitle(QCoreApplication.translate("TrainingDojo", u"OCR Data Training Dojo", None))
        self.lineEdit_text.setPlaceholderText(QCoreApplication.translate("TrainingDojo", u"Text...", None))
        self.pushButton_prev.setText(QCoreApplication.translate("TrainingDojo", u"<", None))
        self.pushButton_next.setText(QCoreApplication.translate("TrainingDojo", u">", None))
        self.pushButton_onlyUndone.setText(QCoreApplication.translate("TrainingDojo", u"Only Undone", None))
    # retranslateUi

