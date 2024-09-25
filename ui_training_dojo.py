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
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TrainingDojo(object):
    def setupUi(self, TrainingDojo):
        if not TrainingDojo.objectName():
            TrainingDojo.setObjectName(u"TrainingDojo")
        TrainingDojo.resize(652, 410)
        self.gridLayout = QGridLayout(TrainingDojo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_files = QListWidget(TrainingDojo)
        self.listWidget_files.setObjectName(u"listWidget_files")

        self.gridLayout.addWidget(self.listWidget_files, 1, 0, 1, 1)

        self.widget = QWidget(TrainingDojo)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_image = QWidget(self.widget)
        self.widget_image.setObjectName(u"widget_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_image.sizePolicy().hasHeightForWidth())
        self.widget_image.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.widget_image)

        self.lineEdit_text = QLineEdit(self.widget)
        self.lineEdit_text.setObjectName(u"lineEdit_text")
        font = QFont()
        font.setPointSize(29)
        self.lineEdit_text.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_text)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_onlyUndone.sizePolicy().hasHeightForWidth())
        self.pushButton_onlyUndone.setSizePolicy(sizePolicy2)
        self.pushButton_onlyUndone.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_onlyUndone, 2, 0, 1, 1)


        self.retranslateUi(TrainingDojo)

        QMetaObject.connectSlotsByName(TrainingDojo)
    # setupUi

    def retranslateUi(self, TrainingDojo):
        TrainingDojo.setWindowTitle(QCoreApplication.translate("TrainingDojo", u"Dialog", None))
        self.lineEdit_text.setPlaceholderText(QCoreApplication.translate("TrainingDojo", u"Text...", None))
        self.pushButton_prev.setText(QCoreApplication.translate("TrainingDojo", u"<", None))
        self.pushButton_next.setText(QCoreApplication.translate("TrainingDojo", u">", None))
        self.pushButton_onlyUndone.setText(QCoreApplication.translate("TrainingDojo", u"Only Undone", None))
    # retranslateUi

