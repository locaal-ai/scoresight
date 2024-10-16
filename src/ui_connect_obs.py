# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_obs.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lineEdit_ip = QLineEdit(self.groupBox)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_ip)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_port = QLineEdit(self.groupBox)
        self.lineEdit_port.setObjectName(u"lineEdit_port")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_port)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_password = QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_password)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.pushButton_connect = QPushButton(self.groupBox)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_connect, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.label_error = QLabel(Dialog)
        self.label_error.setObjectName(u"label_error")
        sizePolicy.setHeightForWidth(self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_error)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Connect OBS", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Websocket Server", None))
        self.lineEdit_ip.setText(QCoreApplication.translate("Dialog", u"localhost", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"IP", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.lineEdit_port.setText(QCoreApplication.translate("Dialog", u"4455", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.pushButton_connect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.label_error.setText("")
    # retranslateUi

