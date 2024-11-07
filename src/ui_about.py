# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
        Dialog.resize(400, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(400, 16777215))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 374, 830))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">About ScoreSight</span></p><p>ScoreSight is an OCR software designed to simplify visual reading of scoreboards and live screencasts.</p><p><span style=\" font-weight:600;\">License</span></p><p>MIT License<br/><br/>Copyright (c) 2024 <a href=\"https://locaal.ai\"><span style=\" text-decoration: underline; color:#007af4;\">Locaal AI</span></a>: AI tools for Developers and Creators</p><p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:<br/><br/>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.<b"
                        "r/><br/>THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p><p><span style=\" font-weight:600;\">Third-Party Software</span><br/>ScoreSight incorporates components from third-party sources under their respective licenses:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">OpenCV</span> is used under the Apache 2 License, permitting the use, distribution, and modification of the soft"
                        "ware provided that certain conditions are met. More information can be found at OpenCV License.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tesseract OCR</span> is used under the Apache 2 License, which allows for the use, distribution, and modification of the software in accordance with the terms set forth in the license. More details are available at Tesseract OCR License.</li></ul><p>Detailed licensing information for these components is included within the software distribution.</p><p><span style=\" font-weight:696;\">Qt Application Framework</span></p><p>This application uses the Qt application framework, which is a comprehensive C++ library for cross-platform development of GUI applications. Qt is used under the terms of the GNU Lesser General Public License (LGPL) version 3. Qt is a registered trademark of The Qt Company Ltd and is developed and maintained by The Qt Project and various c"
                        "ontributors.</p><p>For more information about Qt, including source code of Qt libraries used by this application and guidance on how to obtain or replace Qt libraries, please visit the Qt Project's official website at <a href=\"http://www.qt.io/\"><span style=\" text-decoration: underline; color:#007af4;\">http://www.qt.io</span></a>.</p><p>We are committed to ensuring compliance with the LGPL v3 license and support the principles of open source software development. If you have any questions or concerns regarding our use of Qt, please contact us directly.</p><p><span style=\" font-weight:600;\">Disclaimer of Warranty</span><br/>ScoreSight is provided &quot;AS IS&quot;, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall Roy Shilkrot be liable for any claim, damages, or other liability, whether in an action of contract, tort or otherwise, arising from, out of, or in connection "
                        "with the software or the use or other dealings in the software.</p><p><span style=\" font-weight:600;\">Contact Information</span><br/>For support, feedback, or more information, please visit <a href=\"https://scoresight.live/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://scoresight.live</span></a> or contact us at <a href=\"mailto:info@scoresight.live\"><span style=\" text-decoration: underline; color:#0000ff;\">info@scoresight.live</span></a>.</p></body></html>", None))
    # retranslateUi

