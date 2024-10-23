# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_available.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 418)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Dialog)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.label_newVersion = QLabel(Dialog)
        self.label_newVersion.setObjectName(u"label_newVersion")
        self.label_newVersion.setFrameShape(QFrame.NoFrame)
        self.label_newVersion.setTextFormat(Qt.MarkdownText)
        self.label_newVersion.setMargin(0)
        self.label_newVersion.setIndent(-1)
        self.label_newVersion.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_newVersion, 0, 0, 1, 1)

        self.label_noNewVersion = QLabel(Dialog)
        self.label_noNewVersion.setObjectName(u"label_noNewVersion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_noNewVersion.sizePolicy().hasHeightForWidth())
        self.label_noNewVersion.setSizePolicy(sizePolicy1)
        self.label_noNewVersion.setFrameShape(QFrame.NoFrame)
        self.label_noNewVersion.setTextFormat(Qt.RichText)
        self.label_noNewVersion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_noNewVersion.setMargin(0)
        self.label_noNewVersion.setIndent(-1)

        self.gridLayout.addWidget(self.label_noNewVersion, 1, 0, 1, 1)

        self.checkBox_disableUpdateChecks = QCheckBox(Dialog)
        self.checkBox_disableUpdateChecks.setObjectName(u"checkBox_disableUpdateChecks")

        self.gridLayout.addWidget(self.checkBox_disableUpdateChecks, 4, 0, 1, 1)

        self.label_error = QLabel(Dialog)
        self.label_error.setObjectName(u"label_error")

        self.gridLayout.addWidget(self.label_error, 2, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Update Available", None))
        self.label_newVersion.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>New version of ScoreSight is available!</p><p>Download:</p><p><a href=\"https://download.scoresight.live/scoresight-windows-latest.zip\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-windows-latest.zip</span></a></p><p><a href=\"https://download.scoresight.live/scoresight-macos-x86-latest.dmg\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-macos-x86-latest.dmg</span></a></p><p><a href=\"https://download.scoresight.live/scoresight-linux-latest.tar\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-linux-latest.tar</span></a></p><p>Your configuration will transfer to the new version.</p></body></html>", None))
        self.label_noNewVersion.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>You are already running the latest version.</p><p>However, you can always download the latest version from:</p><p><a href=\"https://download.scoresight.live/scoresight-windows-latest.zip\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-windows-latest.zip</span></a></p><p><a href=\"https://download.scoresight.live/scoresight-macos-x86-latest.dmg\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-macos-x86-latest.dmg</span></a></p><p><a href=\"https://download.scoresight.live/scoresight-linux-latest.tar\"><span style=\" text-decoration: underline; color:#0000ff;\">https://download.scoresight.live/scoresight-linux-latest.tar</span></a></p></body></html>", None))
        self.checkBox_disableUpdateChecks.setText(QCoreApplication.translate("Dialog", u"Disable update checks", None))
        self.label_error.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">Error: Cannot check for updates. Please contact out support team.</span></p></body></html>", None))
    # retranslateUi

