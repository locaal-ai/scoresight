# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 824)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_sb_info = QGroupBox(self.frame)
        self.groupBox_sb_info.setObjectName(u"groupBox_sb_info")
        self.groupBox_sb_info.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_sb_info)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.widget = QWidget(self.groupBox_sb_info)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_boxes = QTableWidget(self.widget)
        if (self.tableWidget_boxes.columnCount() < 2):
            self.tableWidget_boxes.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_boxes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_boxes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_boxes.setObjectName(u"tableWidget_boxes")
        self.tableWidget_boxes.setMinimumSize(QSize(0, 100))
        self.tableWidget_boxes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_boxes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_boxes.setTabKeyNavigation(False)
        self.tableWidget_boxes.setDragDropOverwriteMode(False)
        self.tableWidget_boxes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_boxes.setShowGrid(False)
        self.tableWidget_boxes.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_boxes.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.tableWidget_boxes)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.widget_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(3, 0, 0, 0)
        self.toolButton_addBox = QToolButton(self.widget_8)
        self.toolButton_addBox.setObjectName(u"toolButton_addBox")
        self.toolButton_addBox.setMinimumSize(QSize(27, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.toolButton_addBox.setFont(font)

        self.gridLayout_4.addWidget(self.toolButton_addBox, 0, 0, 1, 1)

        self.toolButton_removeBox = QToolButton(self.widget_8)
        self.toolButton_removeBox.setObjectName(u"toolButton_removeBox")
        self.toolButton_removeBox.setMinimumSize(QSize(27, 0))
        self.toolButton_removeBox.setFont(font)

        self.gridLayout_4.addWidget(self.toolButton_removeBox, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_8, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox_sb_info)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_makeBox = QPushButton(self.widget_2)
        self.pushButton_makeBox.setObjectName(u"pushButton_makeBox")
        self.pushButton_makeBox.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_makeBox)

        self.pushButton_removeBox = QPushButton(self.widget_2)
        self.pushButton_removeBox.setObjectName(u"pushButton_removeBox")
        self.pushButton_removeBox.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_removeBox)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.groupBox_target_settings = QGroupBox(self.groupBox_sb_info)
        self.groupBox_target_settings.setObjectName(u"groupBox_target_settings")
        self.groupBox_target_settings.setCheckable(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_target_settings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.widget_10 = QWidget(self.groupBox_target_settings)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_selectedInfo = QLabel(self.widget_10)
        self.label_selectedInfo.setObjectName(u"label_selectedInfo")

        self.horizontalLayout_12.addWidget(self.label_selectedInfo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.pushButton_restoreDefaults = QPushButton(self.widget_10)
        self.pushButton_restoreDefaults.setObjectName(u"pushButton_restoreDefaults")

        self.horizontalLayout_12.addWidget(self.pushButton_restoreDefaults)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.groupBox_target_settings)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEdit_format = QLineEdit(self.widget_7)
        self.lineEdit_format.setObjectName(u"lineEdit_format")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_format.sizePolicy().hasHeightForWidth())
        self.lineEdit_format.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.lineEdit_format)

        self.comboBox_formatPrefix = QComboBox(self.widget_7)
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.addItem("")
        self.comboBox_formatPrefix.setObjectName(u"comboBox_formatPrefix")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_formatPrefix.sizePolicy().hasHeightForWidth())
        self.comboBox_formatPrefix.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.comboBox_formatPrefix)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.widget_19 = QWidget(self.groupBox_target_settings)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_19)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_21.addWidget(self.label_13)

        self.comboBox_fieldType = QComboBox(self.widget_19)
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.setObjectName(u"comboBox_fieldType")

        self.horizontalLayout_21.addWidget(self.comboBox_fieldType)


        self.verticalLayout_5.addWidget(self.widget_19)

        self.widget_14 = QWidget(self.groupBox_target_settings)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy2.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy2)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_16.setSpacing(3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_smoothing = QCheckBox(self.widget_14)
        self.checkBox_smoothing.setObjectName(u"checkBox_smoothing")

        self.horizontalLayout_16.addWidget(self.checkBox_smoothing)

        self.checkBox_ordinalIndicator = QCheckBox(self.widget_14)
        self.checkBox_ordinalIndicator.setObjectName(u"checkBox_ordinalIndicator")

        self.horizontalLayout_16.addWidget(self.checkBox_ordinalIndicator)


        self.verticalLayout_5.addWidget(self.widget_14)

        self.widget_11 = QWidget(self.groupBox_target_settings)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy2.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.checkBox_skip_empty = QCheckBox(self.widget_11)
        self.checkBox_skip_empty.setObjectName(u"checkBox_skip_empty")

        self.horizontalLayout_13.addWidget(self.checkBox_skip_empty)

        self.checkBox_skip_similar_image = QCheckBox(self.widget_11)
        self.checkBox_skip_similar_image.setObjectName(u"checkBox_skip_similar_image")

        self.horizontalLayout_13.addWidget(self.checkBox_skip_similar_image)


        self.verticalLayout_5.addWidget(self.widget_11)

        self.widget_15 = QWidget(self.groupBox_target_settings)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.checkBox_autocrop = QCheckBox(self.widget_15)
        self.checkBox_autocrop.setObjectName(u"checkBox_autocrop")

        self.horizontalLayout_17.addWidget(self.checkBox_autocrop)

        self.checkBox_invertPatch = QCheckBox(self.widget_15)
        self.checkBox_invertPatch.setObjectName(u"checkBox_invertPatch")

        self.horizontalLayout_17.addWidget(self.checkBox_invertPatch)


        self.verticalLayout_5.addWidget(self.widget_15)

        self.checkBox_removeLeadingZeros = QCheckBox(self.groupBox_target_settings)
        self.checkBox_removeLeadingZeros.setObjectName(u"checkBox_removeLeadingZeros")

        self.verticalLayout_5.addWidget(self.checkBox_removeLeadingZeros)

        self.widget_9 = QWidget(self.groupBox_target_settings)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox_rescalePatch = QCheckBox(self.widget_9)
        self.checkBox_rescalePatch.setObjectName(u"checkBox_rescalePatch")

        self.horizontalLayout_11.addWidget(self.checkBox_rescalePatch)

        self.checkBox_normWHRatio = QCheckBox(self.widget_9)
        self.checkBox_normWHRatio.setObjectName(u"checkBox_normWHRatio")

        self.horizontalLayout_11.addWidget(self.checkBox_normWHRatio)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_20 = QWidget(self.groupBox_target_settings)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_binarizationMethod = QLabel(self.widget_20)
        self.label_binarizationMethod.setObjectName(u"label_binarizationMethod")

        self.horizontalLayout_23.addWidget(self.label_binarizationMethod)

        self.comboBox_binarizationMethod = QComboBox(self.widget_20)
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.setObjectName(u"comboBox_binarizationMethod")

        self.horizontalLayout_23.addWidget(self.comboBox_binarizationMethod)


        self.verticalLayout_5.addWidget(self.widget_20)

        self.widget_17 = QWidget(self.groupBox_target_settings)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy3.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy3)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_20.addWidget(self.label_4)

        self.horizontalSlider_cleanup = QSlider(self.widget_17)
        self.horizontalSlider_cleanup.setObjectName(u"horizontalSlider_cleanup")
        self.horizontalSlider_cleanup.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.horizontalSlider_cleanup)

        self.label_15 = QLabel(self.widget_17)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.horizontalSlider_vscale = QSlider(self.widget_17)
        self.horizontalSlider_vscale.setObjectName(u"horizontalSlider_vscale")
        self.horizontalSlider_vscale.setMinimum(1)
        self.horizontalSlider_vscale.setMaximum(10)
        self.horizontalSlider_vscale.setPageStep(5)
        self.horizontalSlider_vscale.setValue(10)
        self.horizontalSlider_vscale.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.horizontalSlider_vscale)


        self.verticalLayout_5.addWidget(self.widget_17)

        self.widget_13 = QWidget(self.groupBox_target_settings)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.horizontalSlider_dilate = QSlider(self.widget_13)
        self.horizontalSlider_dilate.setObjectName(u"horizontalSlider_dilate")
        self.horizontalSlider_dilate.setMaximum(5)
        self.horizontalSlider_dilate.setPageStep(1)
        self.horizontalSlider_dilate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_dilate)

        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSlider_skew = QSlider(self.widget_13)
        self.horizontalSlider_skew.setObjectName(u"horizontalSlider_skew")
        self.horizontalSlider_skew.setMinimum(-10)
        self.horizontalSlider_skew.setMaximum(10)
        self.horizontalSlider_skew.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_skew)


        self.verticalLayout_5.addWidget(self.widget_13)

        self.widget_21 = QWidget(self.groupBox_target_settings)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_21)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.horizontalSlider_conf_thresh = QSlider(self.widget_21)
        self.horizontalSlider_conf_thresh.setObjectName(u"horizontalSlider_conf_thresh")
        self.horizontalSlider_conf_thresh.setValue(50)
        self.horizontalSlider_conf_thresh.setOrientation(Qt.Horizontal)

        self.horizontalLayout_24.addWidget(self.horizontalSlider_conf_thresh)


        self.verticalLayout_5.addWidget(self.widget_21)


        self.verticalLayout_3.addWidget(self.groupBox_target_settings)

        self.widget_6 = QWidget(self.groupBox_sb_info)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.comboBox_ocrModel = QComboBox(self.widget_6)
        self.comboBox_ocrModel.setObjectName(u"comboBox_ocrModel")

        self.horizontalLayout_7.addWidget(self.comboBox_ocrModel)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.groupBox_sb_info)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.tabWidget_outputs = QTabWidget(self.frame)
        self.tabWidget_outputs.setObjectName(u"tabWidget_outputs")
        sizePolicy3.setHeightForWidth(self.tabWidget_outputs.sizePolicy().hasHeightForWidth())
        self.tabWidget_outputs.setSizePolicy(sizePolicy3)
        self.tabWidget_outputs.setTabShape(QTabWidget.Rounded)
        self.tab_textFiles = QWidget()
        self.tab_textFiles.setObjectName(u"tab_textFiles")
        sizePolicy3.setHeightForWidth(self.tab_textFiles.sizePolicy().hasHeightForWidth())
        self.tab_textFiles.setSizePolicy(sizePolicy3)
        self.formLayout_2 = QFormLayout(self.tab_textFiles)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(self.tab_textFiles)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.widget_5 = QWidget(self.tab_textFiles)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_folder = QLineEdit(self.widget_5)
        self.lineEdit_folder.setObjectName(u"lineEdit_folder")
        self.lineEdit_folder.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_folder)

        self.pushButton_selectFolder = QToolButton(self.widget_5)
        self.pushButton_selectFolder.setObjectName(u"pushButton_selectFolder")

        self.horizontalLayout_6.addWidget(self.pushButton_selectFolder)

        self.toolButton_trashFolder = QToolButton(self.widget_5)
        self.toolButton_trashFolder.setObjectName(u"toolButton_trashFolder")

        self.horizontalLayout_6.addWidget(self.toolButton_trashFolder)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.widget_5)

        self.widget_12 = QWidget(self.tab_textFiles)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy4.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy4)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.checkBox_saveCsv = QCheckBox(self.widget_12)
        self.checkBox_saveCsv.setObjectName(u"checkBox_saveCsv")

        self.horizontalLayout_14.addWidget(self.checkBox_saveCsv)

        self.checkBox_saveXML = QCheckBox(self.widget_12)
        self.checkBox_saveXML.setObjectName(u"checkBox_saveXML")

        self.horizontalLayout_14.addWidget(self.checkBox_saveXML)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.widget_12)

        self.label_append = QLabel(self.tab_textFiles)
        self.label_append.setObjectName(u"label_append")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_append)

        self.comboBox_appendMethod = QComboBox(self.tab_textFiles)
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.setObjectName(u"comboBox_appendMethod")
        sizePolicy4.setHeightForWidth(self.comboBox_appendMethod.sizePolicy().hasHeightForWidth())
        self.comboBox_appendMethod.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBox_appendMethod)

        self.label_savePerSec = QLabel(self.tab_textFiles)
        self.label_savePerSec.setObjectName(u"label_savePerSec")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_savePerSec)

        self.horizontalSlider_aggsPerSecond = QSlider(self.tab_textFiles)
        self.horizontalSlider_aggsPerSecond.setObjectName(u"horizontalSlider_aggsPerSecond")
        self.horizontalSlider_aggsPerSecond.setMinimum(1)
        self.horizontalSlider_aggsPerSecond.setMaximum(10)
        self.horizontalSlider_aggsPerSecond.setPageStep(1)
        self.horizontalSlider_aggsPerSecond.setValue(5)
        self.horizontalSlider_aggsPerSecond.setOrientation(Qt.Horizontal)
        self.horizontalSlider_aggsPerSecond.setTickPosition(QSlider.TicksBelow)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.horizontalSlider_aggsPerSecond)

        self.tabWidget_outputs.addTab(self.tab_textFiles, "")
        self.tab_browser = QWidget()
        self.tab_browser.setObjectName(u"tab_browser")
        self.verticalLayout_4 = QVBoxLayout(self.tab_browser)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.tab_browser)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignTop)

        self.tabWidget_outputs.addTab(self.tab_browser, "")
        self.tab_obs = QWidget()
        self.tab_obs.setObjectName(u"tab_obs")
        self.gridLayout_2 = QGridLayout(self.tab_obs)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(2)
        self.pushButton_connectObs = QPushButton(self.tab_obs)
        self.pushButton_connectObs.setObjectName(u"pushButton_connectObs")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_connectObs.sizePolicy().hasHeightForWidth())
        self.pushButton_connectObs.setSizePolicy(sizePolicy6)
        self.pushButton_connectObs.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.pushButton_connectObs, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.tab_obs)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lineEdit_sceneName = QLineEdit(self.widget_18)
        self.lineEdit_sceneName.setObjectName(u"lineEdit_sceneName")
        self.lineEdit_sceneName.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.lineEdit_sceneName)

        self.pushButton_createOBSScene = QPushButton(self.widget_18)
        self.pushButton_createOBSScene.setObjectName(u"pushButton_createOBSScene")
        self.pushButton_createOBSScene.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.pushButton_createOBSScene)

        self.checkBox_recreate = QCheckBox(self.widget_18)
        self.checkBox_recreate.setObjectName(u"checkBox_recreate")
        self.checkBox_recreate.setEnabled(False)
        self.checkBox_recreate.setChecked(True)

        self.horizontalLayout_22.addWidget(self.checkBox_recreate)


        self.gridLayout_2.addWidget(self.widget_18, 1, 0, 1, 1, Qt.AlignTop)

        self.tabWidget_outputs.addTab(self.tab_obs, "")
        self.tab_vmix = QWidget()
        self.tab_vmix.setObjectName(u"tab_vmix")
        self.gridLayout_3 = QGridLayout(self.tab_vmix)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(2)
        self.tableView_vmixMapping = QTableView(self.tab_vmix)
        self.tableView_vmixMapping.setObjectName(u"tableView_vmixMapping")
        self.tableView_vmixMapping.horizontalHeader().setVisible(False)
        self.tableView_vmixMapping.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableView_vmixMapping, 2, 0, 1, 1)

        self.widget_16 = QWidget(self.tab_vmix)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.widget_16, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connectionLabel = QLabel(self.tab_vmix)
        self.connectionLabel.setObjectName(u"connectionLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.connectionLabel)

        self.connectionWidget = QWidget(self.tab_vmix)
        self.connectionWidget.setObjectName(u"connectionWidget")
        self.horizontalLayout_18 = QHBoxLayout(self.connectionWidget)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_vmixHost = QLineEdit(self.connectionWidget)
        self.lineEdit_vmixHost.setObjectName(u"lineEdit_vmixHost")

        self.horizontalLayout_18.addWidget(self.lineEdit_vmixHost)

        self.label_5 = QLabel(self.connectionWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.lineEdit_vmixPort = QLineEdit(self.connectionWidget)
        self.lineEdit_vmixPort.setObjectName(u"lineEdit_vmixPort")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit_vmixPort.sizePolicy().hasHeightForWidth())
        self.lineEdit_vmixPort.setSizePolicy(sizePolicy7)
        self.lineEdit_vmixPort.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEdit_vmixPort)

        self.pushButton_startvmix = QPushButton(self.connectionWidget)
        self.pushButton_startvmix.setObjectName(u"pushButton_startvmix")
        sizePolicy7.setHeightForWidth(self.pushButton_startvmix.sizePolicy().hasHeightForWidth())
        self.pushButton_startvmix.setSizePolicy(sizePolicy7)
        self.pushButton_startvmix.setCheckable(True)
        self.pushButton_startvmix.setChecked(False)

        self.horizontalLayout_18.addWidget(self.pushButton_startvmix)


        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.connectionWidget)

        self.vmixinputLabel = QLabel(self.tab_vmix)
        self.vmixinputLabel.setObjectName(u"vmixinputLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.vmixinputLabel)

        self.inputLineEdit_vmix = QLineEdit(self.tab_vmix)
        self.inputLineEdit_vmix.setObjectName(u"inputLineEdit_vmix")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.inputLineEdit_vmix)


        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.tabWidget_outputs.addTab(self.tab_vmix, "")

        self.verticalLayout.addWidget(self.tabWidget_outputs, 0, Qt.AlignTop)

        self.pushButton_stopUpdates = QPushButton(self.frame)
        self.pushButton_stopUpdates.setObjectName(u"pushButton_stopUpdates")
        self.pushButton_stopUpdates.setMinimumSize(QSize(0, 0))
        self.pushButton_stopUpdates.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_stopUpdates)

        self.widget_detectionCadence = QWidget(self.frame)
        self.widget_detectionCadence.setObjectName(u"widget_detectionCadence")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_detectionCadence)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_detectionCadence = QLabel(self.widget_detectionCadence)
        self.label_detectionCadence.setObjectName(u"label_detectionCadence")

        self.horizontalLayout_9.addWidget(self.label_detectionCadence)

        self.horizontalSlider_detectionCadence = QSlider(self.widget_detectionCadence)
        self.horizontalSlider_detectionCadence.setObjectName(u"horizontalSlider_detectionCadence")
        self.horizontalSlider_detectionCadence.setMinimum(1)
        self.horizontalSlider_detectionCadence.setMaximum(15)
        self.horizontalSlider_detectionCadence.setPageStep(5)
        self.horizontalSlider_detectionCadence.setValue(5)
        self.horizontalSlider_detectionCadence.setOrientation(Qt.Horizontal)
        self.horizontalSlider_detectionCadence.setInvertedAppearance(False)
        self.horizontalSlider_detectionCadence.setInvertedControls(False)
        self.horizontalSlider_detectionCadence.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_detectionCadence.setTickInterval(5)

        self.horizontalLayout_9.addWidget(self.horizontalSlider_detectionCadence)

        self.checkBox_updateOnchange = QCheckBox(self.widget_detectionCadence)
        self.checkBox_updateOnchange.setObjectName(u"checkBox_updateOnchange")
        self.checkBox_updateOnchange.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBox_updateOnchange)


        self.verticalLayout.addWidget(self.widget_detectionCadence)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_source_view = QFrame(self.centralwidget)
        self.frame_source_view.setObjectName(u"frame_source_view")
        self.frame_source_view.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_source_view.sizePolicy().hasHeightForWidth())
        self.frame_source_view.setSizePolicy(sizePolicy2)
        self.frame_source_view.setFrameShape(QFrame.StyledPanel)
        self.frame_source_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_source_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.widget_4 = QWidget(self.frame_source_view)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox_camera_source = QComboBox(self.widget_3)
        self.comboBox_camera_source.setObjectName(u"comboBox_camera_source")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.comboBox_camera_source.sizePolicy().hasHeightForWidth())
        self.comboBox_camera_source.setSizePolicy(sizePolicy8)

        self.horizontalLayout_3.addWidget(self.comboBox_camera_source)

        self.pushButton_refresh_sources = QToolButton(self.widget_3)
        self.pushButton_refresh_sources.setObjectName(u"pushButton_refresh_sources")

        self.horizontalLayout_3.addWidget(self.pushButton_refresh_sources)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_viewTools = QWidget(self.frame_source_view)
        self.widget_viewTools.setObjectName(u"widget_viewTools")
        self.widget_viewTools.setEnabled(False)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_viewTools)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 3)
        self.pushButton_binary = QPushButton(self.widget_viewTools)
        self.pushButton_binary.setObjectName(u"pushButton_binary")
        self.pushButton_binary.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.pushButton_binary.sizePolicy().hasHeightForWidth())
        self.pushButton_binary.setSizePolicy(sizePolicy7)
        self.pushButton_binary.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_binary)

        self.pushButton_fourCorner = QPushButton(self.widget_viewTools)
        self.pushButton_fourCorner.setObjectName(u"pushButton_fourCorner")
        self.pushButton_fourCorner.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.pushButton_fourCorner.sizePolicy().hasHeightForWidth())
        self.pushButton_fourCorner.setSizePolicy(sizePolicy7)
        self.pushButton_fourCorner.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_fourCorner)

        self.pushButton_stabilize = QPushButton(self.widget_viewTools)
        self.pushButton_stabilize.setObjectName(u"pushButton_stabilize")
        self.pushButton_stabilize.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.pushButton_stabilize.sizePolicy().hasHeightForWidth())
        self.pushButton_stabilize.setSizePolicy(sizePolicy7)
        self.pushButton_stabilize.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_stabilize)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.toolButton_osd = QToolButton(self.widget_viewTools)
        self.toolButton_osd.setObjectName(u"toolButton_osd")
        self.toolButton_osd.setCheckable(True)
        self.toolButton_osd.setChecked(True)

        self.horizontalLayout_10.addWidget(self.toolButton_osd)

        self.toolButton_showOCRrects = QToolButton(self.widget_viewTools)
        self.toolButton_showOCRrects.setObjectName(u"toolButton_showOCRrects")
        self.toolButton_showOCRrects.setCheckable(True)
        self.toolButton_showOCRrects.setChecked(True)

        self.horizontalLayout_10.addWidget(self.toolButton_showOCRrects)

        self.toolButton_zoomReset = QToolButton(self.widget_viewTools)
        self.toolButton_zoomReset.setObjectName(u"toolButton_zoomReset")

        self.horizontalLayout_10.addWidget(self.toolButton_zoomReset)

        self.label_11 = QLabel(self.widget_viewTools)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_2.addWidget(self.widget_viewTools)

        self.frame_for_source_view_label = QFrame(self.frame_source_view)
        self.frame_for_source_view_label.setObjectName(u"frame_for_source_view_label")
        self.frame_for_source_view_label.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_for_source_view_label.sizePolicy().hasHeightForWidth())
        self.frame_for_source_view_label.setSizePolicy(sizePolicy9)
        self.frame_for_source_view_label.setFrameShape(QFrame.StyledPanel)
        self.frame_for_source_view_label.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_for_source_view_label)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_for_source_view_label)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setTextFormat(Qt.MarkdownText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_for_source_view_label)


        self.horizontalLayout.addWidget(self.frame_source_view)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_formatPrefix.setCurrentIndex(0)
        self.tabWidget_outputs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScoreSight", None))
        self.groupBox_sb_info.setTitle(QCoreApplication.translate("MainWindow", u"Scoreboard Information", None))
        ___qtablewidgetitem = self.tableWidget_boxes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Field", None));
        ___qtablewidgetitem1 = self.tableWidget_boxes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.toolButton_addBox.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_removeBox.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_makeBox.setText(QCoreApplication.translate("MainWindow", u"Add to Scene ->", None))
        self.pushButton_removeBox.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.groupBox_target_settings.setTitle(QCoreApplication.translate("MainWindow", u"Target Information Settings", None))
        self.label_selectedInfo.setText(QCoreApplication.translate("MainWindow", u"Select an item above", None))
        self.pushButton_restoreDefaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.comboBox_formatPrefix.setItemText(0, QCoreApplication.translate("MainWindow", u"Time mm:ss.d", None))
        self.comboBox_formatPrefix.setItemText(1, QCoreApplication.translate("MainWindow", u"Time mm:ss", None))
        self.comboBox_formatPrefix.setItemText(2, QCoreApplication.translate("MainWindow", u"Time ss.d", None))
        self.comboBox_formatPrefix.setItemText(3, QCoreApplication.translate("MainWindow", u"Time 0-59", None))
        self.comboBox_formatPrefix.setItemText(4, QCoreApplication.translate("MainWindow", u"Shotclock 0-39", None))
        self.comboBox_formatPrefix.setItemText(5, QCoreApplication.translate("MainWindow", u"Score 1dd", None))
        self.comboBox_formatPrefix.setItemText(6, QCoreApplication.translate("MainWindow", u"Score ddd", None))
        self.comboBox_formatPrefix.setItemText(7, QCoreApplication.translate("MainWindow", u"Period 1-4", None))
        self.comboBox_formatPrefix.setItemText(8, QCoreApplication.translate("MainWindow", u"Period d", None))
        self.comboBox_formatPrefix.setItemText(9, QCoreApplication.translate("MainWindow", u"Alphanumeric", None))
        self.comboBox_formatPrefix.setItemText(10, QCoreApplication.translate("MainWindow", u"Any text", None))
        self.comboBox_formatPrefix.setItemText(11, QCoreApplication.translate("MainWindow", u"Any number", None))
        self.comboBox_formatPrefix.setItemText(12, QCoreApplication.translate("MainWindow", u"Select Preset", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox_fieldType.setItemText(0, QCoreApplication.translate("MainWindow", u"Number 0-9", None))
        self.comboBox_fieldType.setItemText(1, QCoreApplication.translate("MainWindow", u"Time 0-9 , . :", None))
        self.comboBox_fieldType.setItemText(2, QCoreApplication.translate("MainWindow", u"Text", None))

        self.checkBox_smoothing.setText(QCoreApplication.translate("MainWindow", u"Average Output", None))
        self.checkBox_ordinalIndicator.setText(QCoreApplication.translate("MainWindow", u"Ordinal (1st, 2nd, ..)", None))
        self.checkBox_skip_empty.setText(QCoreApplication.translate("MainWindow", u"Skip Empty Values", None))
        self.checkBox_skip_similar_image.setText(QCoreApplication.translate("MainWindow", u"Skip Similar Image", None))
        self.checkBox_autocrop.setText(QCoreApplication.translate("MainWindow", u"Auto Crop", None))
        self.checkBox_invertPatch.setText(QCoreApplication.translate("MainWindow", u"Invert Input", None))
        self.checkBox_removeLeadingZeros.setText(QCoreApplication.translate("MainWindow", u"Remove leading 0s", None))
#if QT_CONFIG(tooltip)
        self.checkBox_rescalePatch.setToolTip(QCoreApplication.translate("MainWindow", u"Scale the image to 35 pixels height, a favorable size for OCR", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_rescalePatch.setText(QCoreApplication.translate("MainWindow", u"Rescale Input", None))
#if QT_CONFIG(tooltip)
        self.checkBox_normWHRatio.setToolTip(QCoreApplication.translate("MainWindow", u"Scale to a favorable 1:2 width-to-height ratio", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_normWHRatio.setText(QCoreApplication.translate("MainWindow", u"Normalize W-H Ratio", None))
        self.label_binarizationMethod.setText(QCoreApplication.translate("MainWindow", u"Binarize", None))
        self.comboBox_binarizationMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Global", None))
        self.comboBox_binarizationMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"No Binarization", None))
        self.comboBox_binarizationMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"Local", None))
        self.comboBox_binarizationMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Adaptive", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cleanup", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V.Scale", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dilate", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Skew", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Conf. Th", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"OCR Model", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.pushButton_selectFolder.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.toolButton_trashFolder.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.checkBox_saveCsv.setText(QCoreApplication.translate("MainWindow", u"Save .csv file", None))
        self.checkBox_saveXML.setText(QCoreApplication.translate("MainWindow", u"Save .xml file", None))
        self.label_append.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.comboBox_appendMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Results in .csv file", None))
        self.comboBox_appendMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"Results in .txt files", None))
        self.comboBox_appendMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"Results in both", None))
        self.comboBox_appendMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Don't append results", None))

#if QT_CONFIG(tooltip)
        self.label_savePerSec.setToolTip(QCoreApplication.translate("MainWindow", u"How many times per second to save the results to files", None))
#endif // QT_CONFIG(tooltip)
        self.label_savePerSec.setText(QCoreApplication.translate("MainWindow", u"Save / s", None))
        self.tabWidget_outputs.setTabText(self.tabWidget_outputs.indexOf(self.tab_textFiles), QCoreApplication.translate("MainWindow", u"Text Files", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HTML Scoreboard: <a href=\"http://localhost:18099/scoresight\"><span style=\" text-decoration: underline; color:#0000ff;\">http://localhost:18099/scoresight</span></a></p><p>JSON: <a href=\"http://localhost:18099/json\"><span style=\" text-decoration: underline; color:#0000ff;\">http://localhost:18099/json</span></a> (optional: ?pivot)</p><p>XML: <a href=\"http://localhost:18099/xml\"><span style=\" text-decoration: underline; color:#0000ff;\">http://localhost:18099/xml</span></a> (optional: ?pivot)</p><p>CSV: <a href=\"http://localhost:18099/csv\"><span style=\" text-decoration: underline; color:#0000ff;\">http://localhost:18099/csv</span></a></p></body></html>", None))
        self.tabWidget_outputs.setTabText(self.tabWidget_outputs.indexOf(self.tab_browser), QCoreApplication.translate("MainWindow", u"Browser", None))
        self.pushButton_connectObs.setText(QCoreApplication.translate("MainWindow", u"Connect OBS", None))
        self.lineEdit_sceneName.setText(QCoreApplication.translate("MainWindow", u"ScoreSight Scene", None))
        self.pushButton_createOBSScene.setText(QCoreApplication.translate("MainWindow", u"Create OBS Scene", None))
        self.checkBox_recreate.setText(QCoreApplication.translate("MainWindow", u"Recreate", None))
        self.tabWidget_outputs.setTabText(self.tabWidget_outputs.indexOf(self.tab_obs), QCoreApplication.translate("MainWindow", u"OBS", None))
        self.connectionLabel.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.lineEdit_vmixHost.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_vmixPort.setText(QCoreApplication.translate("MainWindow", u"8099", None))
        self.pushButton_startvmix.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.vmixinputLabel.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.inputLineEdit_vmix.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tabWidget_outputs.setTabText(self.tabWidget_outputs.indexOf(self.tab_vmix), QCoreApplication.translate("MainWindow", u"VMix", None))
        self.pushButton_stopUpdates.setText(QCoreApplication.translate("MainWindow", u"Stop Updates", None))
        self.label_detectionCadence.setText(QCoreApplication.translate("MainWindow", u"Detections / s", None))
#if QT_CONFIG(tooltip)
        self.checkBox_updateOnchange.setToolTip(QCoreApplication.translate("MainWindow", u"Only send an update if the field value has changed", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_updateOnchange.setText(QCoreApplication.translate("MainWindow", u"Update on change", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source", None))
#if QT_CONFIG(tooltip)
        self.pushButton_refresh_sources.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh Sources", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_refresh_sources.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.pushButton_binary.setText(QCoreApplication.translate("MainWindow", u"Binary View", None))
        self.pushButton_fourCorner.setText(QCoreApplication.translate("MainWindow", u"4-corner Correction", None))
        self.pushButton_stabilize.setText(QCoreApplication.translate("MainWindow", u"Stabilize", None))
#if QT_CONFIG(tooltip)
        self.toolButton_osd.setToolTip(QCoreApplication.translate("MainWindow", u"Show Statistics", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_osd.setText(QCoreApplication.translate("MainWindow", u"OSD", None))
#if QT_CONFIG(tooltip)
        self.toolButton_showOCRrects.setToolTip(QCoreApplication.translate("MainWindow", u"Show OCR Detection Boxes", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_showOCRrects.setText(QCoreApplication.translate("MainWindow", u"OCR", None))
        self.toolButton_zoomReset.setText(QCoreApplication.translate("MainWindow", u"1:1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ctrl-scroll to zoom", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"### Open a Camera or Load a File", None))
    # retranslateUi

