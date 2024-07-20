# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractSpinBox,
    QApplication,
    QCheckBox,
    QComboBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_sb_info = QWidget(self.frame)
        self.groupBox_sb_info.setObjectName("groupBox_sb_info")
        self.groupBox_sb_info.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_sb_info)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.groupBox_sb_info)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_boxes = QTableWidget(self.widget)
        if self.tableWidget_boxes.columnCount() < 2:
            self.tableWidget_boxes.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_boxes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_boxes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_boxes.setObjectName("tableWidget_boxes")
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
        self.widget_8.setObjectName("widget_8")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.widget_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(3, 0, 0, 0)
        self.toolButton_addBox = QToolButton(self.widget_8)
        self.toolButton_addBox.setObjectName("toolButton_addBox")
        self.toolButton_addBox.setMinimumSize(QSize(27, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.toolButton_addBox.setFont(font)

        self.gridLayout_4.addWidget(self.toolButton_addBox, 0, 0, 1, 1)

        self.toolButton_removeBox = QToolButton(self.widget_8)
        self.toolButton_removeBox.setObjectName("toolButton_removeBox")
        self.toolButton_removeBox.setMinimumSize(QSize(27, 0))
        self.toolButton_removeBox.setFont(font)

        self.gridLayout_4.addWidget(self.toolButton_removeBox, 1, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox_sb_info)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_makeBox = QPushButton(self.widget_2)
        self.pushButton_makeBox.setObjectName("pushButton_makeBox")
        self.pushButton_makeBox.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_makeBox)

        self.pushButton_removeBox = QPushButton(self.widget_2)
        self.pushButton_removeBox.setObjectName("pushButton_removeBox")
        self.pushButton_removeBox.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_removeBox)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.groupBox_target_settings = QGroupBox(self.groupBox_sb_info)
        self.groupBox_target_settings.setObjectName("groupBox_target_settings")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_target_settings)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 3, 3)
        self.widget_10 = QWidget(self.groupBox_target_settings)
        self.widget_10.setObjectName("widget_10")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.label_selectedInfo = QLabel(self.widget_10)
        self.label_selectedInfo.setObjectName("label_selectedInfo")

        self.horizontalLayout_12.addWidget(self.label_selectedInfo)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.pushButton_restoreDefaults = QPushButton(self.widget_10)
        self.pushButton_restoreDefaults.setObjectName("pushButton_restoreDefaults")

        self.horizontalLayout_12.addWidget(self.pushButton_restoreDefaults)

        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.groupBox_target_settings)
        self.widget_7.setObjectName("widget_7")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEdit_format = QLineEdit(self.widget_7)
        self.lineEdit_format.setObjectName("lineEdit_format")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.lineEdit_format.sizePolicy().hasHeightForWidth()
        )
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
        self.comboBox_formatPrefix.setObjectName("comboBox_formatPrefix")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.comboBox_formatPrefix.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_formatPrefix.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.comboBox_formatPrefix)

        self.verticalLayout_5.addWidget(self.widget_7)

        self.widget_19 = QWidget(self.groupBox_target_settings)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_19)
        self.label_13.setObjectName("label_13")

        self.horizontalLayout_21.addWidget(self.label_13)

        self.comboBox_fieldType = QComboBox(self.widget_19)
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.addItem("")
        self.comboBox_fieldType.setObjectName("comboBox_fieldType")

        self.horizontalLayout_21.addWidget(self.comboBox_fieldType)

        self.verticalLayout_5.addWidget(self.widget_19)

        self.widget_14 = QWidget(self.groupBox_target_settings)
        self.widget_14.setObjectName("widget_14")
        sizePolicy2.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy2)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_16.setSpacing(3)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_smoothing = QCheckBox(self.widget_14)
        self.checkBox_smoothing.setObjectName("checkBox_smoothing")

        self.horizontalLayout_16.addWidget(self.checkBox_smoothing)

        self.checkBox_ordinalIndicator = QCheckBox(self.widget_14)
        self.checkBox_ordinalIndicator.setObjectName("checkBox_ordinalIndicator")

        self.horizontalLayout_16.addWidget(self.checkBox_ordinalIndicator)

        self.verticalLayout_5.addWidget(self.widget_14)

        self.widget_11 = QWidget(self.groupBox_target_settings)
        self.widget_11.setObjectName("widget_11")
        sizePolicy2.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.checkBox_skip_empty = QCheckBox(self.widget_11)
        self.checkBox_skip_empty.setObjectName("checkBox_skip_empty")

        self.horizontalLayout_13.addWidget(self.checkBox_skip_empty)

        self.checkBox_skip_similar_image = QCheckBox(self.widget_11)
        self.checkBox_skip_similar_image.setObjectName("checkBox_skip_similar_image")

        self.horizontalLayout_13.addWidget(self.checkBox_skip_similar_image)

        self.verticalLayout_5.addWidget(self.widget_11)

        self.widget_15 = QWidget(self.groupBox_target_settings)
        self.widget_15.setObjectName("widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.checkBox_autocrop = QCheckBox(self.widget_15)
        self.checkBox_autocrop.setObjectName("checkBox_autocrop")

        self.horizontalLayout_17.addWidget(self.checkBox_autocrop)

        self.checkBox_invertPatch = QCheckBox(self.widget_15)
        self.checkBox_invertPatch.setObjectName("checkBox_invertPatch")

        self.horizontalLayout_17.addWidget(self.checkBox_invertPatch)

        self.verticalLayout_5.addWidget(self.widget_15)

        self.widget_22 = QWidget(self.groupBox_target_settings)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_25.setSpacing(3)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.checkBox_removeLeadingZeros = QCheckBox(self.widget_22)
        self.checkBox_removeLeadingZeros.setObjectName("checkBox_removeLeadingZeros")

        self.horizontalLayout_25.addWidget(self.checkBox_removeLeadingZeros)

        self.checkBox_dotDetector = QCheckBox(self.widget_22)
        self.checkBox_dotDetector.setObjectName("checkBox_dotDetector")

        self.horizontalLayout_25.addWidget(self.checkBox_dotDetector)

        self.verticalLayout_5.addWidget(self.widget_22)

        self.widget_9 = QWidget(self.groupBox_target_settings)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox_rescalePatch = QCheckBox(self.widget_9)
        self.checkBox_rescalePatch.setObjectName("checkBox_rescalePatch")

        self.horizontalLayout_11.addWidget(self.checkBox_rescalePatch)

        self.checkBox_normWHRatio = QCheckBox(self.widget_9)
        self.checkBox_normWHRatio.setObjectName("checkBox_normWHRatio")

        self.horizontalLayout_11.addWidget(self.checkBox_normWHRatio)

        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_20 = QWidget(self.groupBox_target_settings)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_binarizationMethod = QLabel(self.widget_20)
        self.label_binarizationMethod.setObjectName("label_binarizationMethod")

        self.horizontalLayout_23.addWidget(self.label_binarizationMethod)

        self.comboBox_binarizationMethod = QComboBox(self.widget_20)
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.addItem("")
        self.comboBox_binarizationMethod.setObjectName("comboBox_binarizationMethod")

        self.horizontalLayout_23.addWidget(self.comboBox_binarizationMethod)

        self.verticalLayout_5.addWidget(self.widget_20)

        self.widget_17 = QWidget(self.groupBox_target_settings)
        self.widget_17.setObjectName("widget_17")
        sizePolicy3.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy3)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_20.addWidget(self.label_4)

        self.horizontalSlider_cleanup = QSlider(self.widget_17)
        self.horizontalSlider_cleanup.setObjectName("horizontalSlider_cleanup")
        self.horizontalSlider_cleanup.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.horizontalSlider_cleanup)

        self.label_15 = QLabel(self.widget_17)
        self.label_15.setObjectName("label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.horizontalSlider_vscale = QSlider(self.widget_17)
        self.horizontalSlider_vscale.setObjectName("horizontalSlider_vscale")
        self.horizontalSlider_vscale.setMinimum(1)
        self.horizontalSlider_vscale.setMaximum(10)
        self.horizontalSlider_vscale.setPageStep(5)
        self.horizontalSlider_vscale.setValue(10)
        self.horizontalSlider_vscale.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.horizontalSlider_vscale)

        self.verticalLayout_5.addWidget(self.widget_17)

        self.widget_13 = QWidget(self.groupBox_target_settings)
        self.widget_13.setObjectName("widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.horizontalSlider_dilate = QSlider(self.widget_13)
        self.horizontalSlider_dilate.setObjectName("horizontalSlider_dilate")
        self.horizontalSlider_dilate.setMaximum(5)
        self.horizontalSlider_dilate.setPageStep(1)
        self.horizontalSlider_dilate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_dilate)

        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName("label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSlider_skew = QSlider(self.widget_13)
        self.horizontalSlider_skew.setObjectName("horizontalSlider_skew")
        self.horizontalSlider_skew.setMinimum(-10)
        self.horizontalSlider_skew.setMaximum(10)
        self.horizontalSlider_skew.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_skew)

        self.verticalLayout_5.addWidget(self.widget_13)

        self.widget_21 = QWidget(self.groupBox_target_settings)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_21)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.horizontalSlider_conf_thresh = QSlider(self.widget_21)
        self.horizontalSlider_conf_thresh.setObjectName("horizontalSlider_conf_thresh")
        self.horizontalSlider_conf_thresh.setValue(50)
        self.horizontalSlider_conf_thresh.setOrientation(Qt.Horizontal)

        self.horizontalLayout_24.addWidget(self.horizontalSlider_conf_thresh)

        self.verticalLayout_5.addWidget(self.widget_21)

        self.verticalLayout_3.addWidget(self.groupBox_target_settings)

        self.widget_6 = QWidget(self.groupBox_sb_info)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName("label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.comboBox_ocrModel = QComboBox(self.widget_6)
        self.comboBox_ocrModel.setObjectName("comboBox_ocrModel")

        self.horizontalLayout_7.addWidget(self.comboBox_ocrModel)

        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalLayout.addWidget(self.groupBox_sb_info)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName("line_2")
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.tabWidget_outputs = QTabWidget(self.frame)
        self.tabWidget_outputs.setObjectName("tabWidget_outputs")
        sizePolicy3.setHeightForWidth(
            self.tabWidget_outputs.sizePolicy().hasHeightForWidth()
        )
        self.tabWidget_outputs.setSizePolicy(sizePolicy3)
        self.tabWidget_outputs.setTabShape(QTabWidget.Rounded)
        self.tab_textFiles = QWidget()
        self.tab_textFiles.setObjectName("tab_textFiles")
        sizePolicy3.setHeightForWidth(
            self.tab_textFiles.sizePolicy().hasHeightForWidth()
        )
        self.tab_textFiles.setSizePolicy(sizePolicy3)
        self.formLayout_2 = QFormLayout(self.tab_textFiles)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(self.tab_textFiles)
        self.label_7.setObjectName("label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.widget_5 = QWidget(self.tab_textFiles)
        self.widget_5.setObjectName("widget_5")
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_folder = QLineEdit(self.widget_5)
        self.lineEdit_folder.setObjectName("lineEdit_folder")
        self.lineEdit_folder.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_folder)

        self.pushButton_selectFolder = QToolButton(self.widget_5)
        self.pushButton_selectFolder.setObjectName("pushButton_selectFolder")

        self.horizontalLayout_6.addWidget(self.pushButton_selectFolder)

        self.toolButton_trashFolder = QToolButton(self.widget_5)
        self.toolButton_trashFolder.setObjectName("toolButton_trashFolder")

        self.horizontalLayout_6.addWidget(self.toolButton_trashFolder)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.widget_5)

        self.widget_12 = QWidget(self.tab_textFiles)
        self.widget_12.setObjectName("widget_12")
        sizePolicy4.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy4)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.checkBox_saveCsv = QCheckBox(self.widget_12)
        self.checkBox_saveCsv.setObjectName("checkBox_saveCsv")

        self.horizontalLayout_14.addWidget(self.checkBox_saveCsv)

        self.checkBox_saveXML = QCheckBox(self.widget_12)
        self.checkBox_saveXML.setObjectName("checkBox_saveXML")

        self.horizontalLayout_14.addWidget(self.checkBox_saveXML)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.widget_12)

        self.label_append = QLabel(self.tab_textFiles)
        self.label_append.setObjectName("label_append")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_append)

        self.comboBox_appendMethod = QComboBox(self.tab_textFiles)
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.addItem("")
        self.comboBox_appendMethod.setObjectName("comboBox_appendMethod")
        sizePolicy4.setHeightForWidth(
            self.comboBox_appendMethod.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_appendMethod.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(
            2, QFormLayout.FieldRole, self.comboBox_appendMethod
        )

        self.label_savePerSec = QLabel(self.tab_textFiles)
        self.label_savePerSec.setObjectName("label_savePerSec")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_savePerSec)

        self.horizontalSlider_aggsPerSecond = QSlider(self.tab_textFiles)
        self.horizontalSlider_aggsPerSecond.setObjectName(
            "horizontalSlider_aggsPerSecond"
        )
        self.horizontalSlider_aggsPerSecond.setMinimum(1)
        self.horizontalSlider_aggsPerSecond.setMaximum(10)
        self.horizontalSlider_aggsPerSecond.setPageStep(1)
        self.horizontalSlider_aggsPerSecond.setValue(5)
        self.horizontalSlider_aggsPerSecond.setOrientation(Qt.Horizontal)
        self.horizontalSlider_aggsPerSecond.setTickPosition(QSlider.TicksBelow)

        self.formLayout_2.setWidget(
            3, QFormLayout.FieldRole, self.horizontalSlider_aggsPerSecond
        )

        self.tabWidget_outputs.addTab(self.tab_textFiles, "")
        self.tab_browser = QWidget()
        self.tab_browser.setObjectName("tab_browser")
        self.verticalLayout_4 = QVBoxLayout(self.tab_browser)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QLabel(self.tab_browser)
        self.label_8.setObjectName("label_8")
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignTop)

        self.tabWidget_outputs.addTab(self.tab_browser, "")
        self.tab_obs = QWidget()
        self.tab_obs.setObjectName("tab_obs")
        self.gridLayout_2 = QGridLayout(self.tab_obs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(2)
        self.pushButton_connectObs = QPushButton(self.tab_obs)
        self.pushButton_connectObs.setObjectName("pushButton_connectObs")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.pushButton_connectObs.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_connectObs.setSizePolicy(sizePolicy6)
        self.pushButton_connectObs.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.pushButton_connectObs, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.tab_obs)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lineEdit_sceneName = QLineEdit(self.widget_18)
        self.lineEdit_sceneName.setObjectName("lineEdit_sceneName")
        self.lineEdit_sceneName.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.lineEdit_sceneName)

        self.pushButton_createOBSScene = QPushButton(self.widget_18)
        self.pushButton_createOBSScene.setObjectName("pushButton_createOBSScene")
        self.pushButton_createOBSScene.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.pushButton_createOBSScene)

        self.checkBox_recreate = QCheckBox(self.widget_18)
        self.checkBox_recreate.setObjectName("checkBox_recreate")
        self.checkBox_recreate.setEnabled(False)
        self.checkBox_recreate.setChecked(True)

        self.horizontalLayout_22.addWidget(self.checkBox_recreate)

        self.gridLayout_2.addWidget(self.widget_18, 1, 0, 1, 1, Qt.AlignTop)

        self.tabWidget_outputs.addTab(self.tab_obs, "")
        self.tab_vmix = QWidget()
        self.tab_vmix.setObjectName("tab_vmix")
        self.gridLayout_3 = QGridLayout(self.tab_vmix)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(2)
        self.tableView_vmixMapping = QTableView(self.tab_vmix)
        self.tableView_vmixMapping.setObjectName("tableView_vmixMapping")
        self.tableView_vmixMapping.horizontalHeader().setVisible(False)
        self.tableView_vmixMapping.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableView_vmixMapping, 2, 0, 1, 1)

        self.widget_16 = QWidget(self.tab_vmix)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.widget_16, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connectionLabel = QLabel(self.tab_vmix)
        self.connectionLabel.setObjectName("connectionLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.connectionLabel)

        self.connectionWidget = QWidget(self.tab_vmix)
        self.connectionWidget.setObjectName("connectionWidget")
        self.horizontalLayout_18 = QHBoxLayout(self.connectionWidget)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_vmixHost = QLineEdit(self.connectionWidget)
        self.lineEdit_vmixHost.setObjectName("lineEdit_vmixHost")

        self.horizontalLayout_18.addWidget(self.lineEdit_vmixHost)

        self.label_5 = QLabel(self.connectionWidget)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.lineEdit_vmixPort = QLineEdit(self.connectionWidget)
        self.lineEdit_vmixPort.setObjectName("lineEdit_vmixPort")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.lineEdit_vmixPort.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_vmixPort.setSizePolicy(sizePolicy7)
        self.lineEdit_vmixPort.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEdit_vmixPort)

        self.pushButton_startvmix = QPushButton(self.connectionWidget)
        self.pushButton_startvmix.setObjectName("pushButton_startvmix")
        sizePolicy7.setHeightForWidth(
            self.pushButton_startvmix.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_startvmix.setSizePolicy(sizePolicy7)
        self.pushButton_startvmix.setCheckable(True)
        self.pushButton_startvmix.setChecked(False)

        self.horizontalLayout_18.addWidget(self.pushButton_startvmix)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.connectionWidget)

        self.vmixinputLabel = QLabel(self.tab_vmix)
        self.vmixinputLabel.setObjectName("vmixinputLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.vmixinputLabel)

        self.inputLineEdit_vmix = QLineEdit(self.tab_vmix)
        self.inputLineEdit_vmix.setObjectName("inputLineEdit_vmix")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.inputLineEdit_vmix)

        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.tabWidget_outputs.addTab(self.tab_vmix, "")

        self.verticalLayout.addWidget(self.tabWidget_outputs, 0, Qt.AlignTop)

        self.pushButton_stopUpdates = QPushButton(self.frame)
        self.pushButton_stopUpdates.setObjectName("pushButton_stopUpdates")
        self.pushButton_stopUpdates.setMinimumSize(QSize(0, 0))
        self.pushButton_stopUpdates.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_stopUpdates)

        self.widget_detectionCadence = QWidget(self.frame)
        self.widget_detectionCadence.setObjectName("widget_detectionCadence")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_detectionCadence)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_detectionCadence = QLabel(self.widget_detectionCadence)
        self.label_detectionCadence.setObjectName("label_detectionCadence")

        self.horizontalLayout_9.addWidget(self.label_detectionCadence)

        self.horizontalSlider_detectionCadence = QSlider(self.widget_detectionCadence)
        self.horizontalSlider_detectionCadence.setObjectName(
            "horizontalSlider_detectionCadence"
        )
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
        self.checkBox_updateOnchange.setObjectName("checkBox_updateOnchange")
        self.checkBox_updateOnchange.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBox_updateOnchange)

        self.verticalLayout.addWidget(self.widget_detectionCadence)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_source_view = QFrame(self.centralwidget)
        self.frame_source_view.setObjectName("frame_source_view")
        self.frame_source_view.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.frame_source_view.sizePolicy().hasHeightForWidth()
        )
        self.frame_source_view.setSizePolicy(sizePolicy2)
        self.frame_source_view.setFrameShape(QFrame.StyledPanel)
        self.frame_source_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_source_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.widget_4 = QWidget(self.frame_source_view)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox_camera_source = QComboBox(self.widget_3)
        self.comboBox_camera_source.addItem("")
        self.comboBox_camera_source.addItem("")
        self.comboBox_camera_source.addItem("")
        self.comboBox_camera_source.addItem("")
        self.comboBox_camera_source.setObjectName("comboBox_camera_source")
        sizePolicy8 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(
            self.comboBox_camera_source.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_camera_source.setSizePolicy(sizePolicy8)

        self.horizontalLayout_3.addWidget(self.comboBox_camera_source)

        self.pushButton_refresh_sources = QToolButton(self.widget_3)
        self.pushButton_refresh_sources.setObjectName("pushButton_refresh_sources")

        self.horizontalLayout_3.addWidget(self.pushButton_refresh_sources)

        self.horizontalLayout_4.addWidget(self.widget_3)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_viewTools = QWidget(self.frame_source_view)
        self.widget_viewTools.setObjectName("widget_viewTools")
        self.widget_viewTools.setEnabled(False)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_viewTools)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 3)
        self.pushButton_binary = QToolButton(self.widget_viewTools)
        self.pushButton_binary.setObjectName("pushButton_binary")
        self.pushButton_binary.setEnabled(False)
        self.pushButton_binary.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_binary)

        self.pushButton_fourCorner = QToolButton(self.widget_viewTools)
        self.pushButton_fourCorner.setObjectName("pushButton_fourCorner")
        self.pushButton_fourCorner.setEnabled(False)
        self.pushButton_fourCorner.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_fourCorner)

        self.toolButton_topCrop = QToolButton(self.widget_viewTools)
        self.toolButton_topCrop.setObjectName("toolButton_topCrop")
        self.toolButton_topCrop.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.toolButton_topCrop)

        self.pushButton_stabilize = QToolButton(self.widget_viewTools)
        self.pushButton_stabilize.setObjectName("pushButton_stabilize")
        self.pushButton_stabilize.setEnabled(False)
        self.pushButton_stabilize.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.pushButton_stabilize)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.toolButton_osd = QToolButton(self.widget_viewTools)
        self.toolButton_osd.setObjectName("toolButton_osd")
        self.toolButton_osd.setCheckable(True)
        self.toolButton_osd.setChecked(True)

        self.horizontalLayout_10.addWidget(self.toolButton_osd)

        self.toolButton_showOCRrects = QToolButton(self.widget_viewTools)
        self.toolButton_showOCRrects.setObjectName("toolButton_showOCRrects")
        self.toolButton_showOCRrects.setCheckable(True)
        self.toolButton_showOCRrects.setChecked(True)

        self.horizontalLayout_10.addWidget(self.toolButton_showOCRrects)

        self.toolButton_zoomReset = QToolButton(self.widget_viewTools)
        self.toolButton_zoomReset.setObjectName("toolButton_zoomReset")

        self.horizontalLayout_10.addWidget(self.toolButton_zoomReset)

        self.label_11 = QLabel(self.widget_viewTools)
        self.label_11.setObjectName("label_11")
        self.label_11.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.verticalLayout_2.addWidget(self.widget_viewTools)

        self.widget_cropPanel = QWidget(self.frame_source_view)
        self.widget_cropPanel.setObjectName("widget_cropPanel")
        self.widget_cropPanel.setEnabled(False)
        self.widget_cropPanel.setMaximumSize(QSize(16777215, 18))
        font1 = QFont()
        font1.setPointSize(8)
        self.widget_cropPanel.setFont(font1)
        self.horizontalLayout_26 = QHBoxLayout(self.widget_cropPanel)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_cropPanel)
        self.label_16.setObjectName("label_16")

        self.horizontalLayout_26.addWidget(self.label_16)

        self.spinBox_leftCrop = QSpinBox(self.widget_cropPanel)
        self.spinBox_leftCrop.setObjectName("spinBox_leftCrop")
        self.spinBox_leftCrop.setMinimumSize(QSize(70, 0))
        self.spinBox_leftCrop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_leftCrop.setMaximum(999)

        self.horizontalLayout_26.addWidget(self.spinBox_leftCrop)

        self.label_17 = QLabel(self.widget_cropPanel)
        self.label_17.setObjectName("label_17")

        self.horizontalLayout_26.addWidget(self.label_17)

        self.spinBox_topCrop = QSpinBox(self.widget_cropPanel)
        self.spinBox_topCrop.setObjectName("spinBox_topCrop")
        self.spinBox_topCrop.setMinimumSize(QSize(70, 0))
        self.spinBox_topCrop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_topCrop.setMaximum(999)

        self.horizontalLayout_26.addWidget(self.spinBox_topCrop)

        self.label_18 = QLabel(self.widget_cropPanel)
        self.label_18.setObjectName("label_18")

        self.horizontalLayout_26.addWidget(self.label_18)

        self.spinBox_rightCrop = QSpinBox(self.widget_cropPanel)
        self.spinBox_rightCrop.setObjectName("spinBox_rightCrop")
        self.spinBox_rightCrop.setMinimumSize(QSize(70, 0))
        self.spinBox_rightCrop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_rightCrop.setMaximum(999)

        self.horizontalLayout_26.addWidget(self.spinBox_rightCrop)

        self.label_19 = QLabel(self.widget_cropPanel)
        self.label_19.setObjectName("label_19")

        self.horizontalLayout_26.addWidget(self.label_19)

        self.spinBox_bottomCrop = QSpinBox(self.widget_cropPanel)
        self.spinBox_bottomCrop.setObjectName("spinBox_bottomCrop")
        self.spinBox_bottomCrop.setMinimumSize(QSize(70, 0))
        self.spinBox_bottomCrop.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_bottomCrop.setMaximum(999)

        self.horizontalLayout_26.addWidget(self.spinBox_bottomCrop)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_26.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addWidget(self.widget_cropPanel)

        self.frame_for_source_view_label = QFrame(self.frame_source_view)
        self.frame_for_source_view_label.setObjectName("frame_for_source_view_label")
        self.frame_for_source_view_label.setEnabled(True)
        sizePolicy9 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.frame_for_source_view_label.sizePolicy().hasHeightForWidth()
        )
        self.frame_for_source_view_label.setSizePolicy(sizePolicy9)
        self.gridLayout = QGridLayout(self.frame_for_source_view_label)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_for_source_view_label)
        self.label_12.setObjectName("label_12")
        self.label_12.setEnabled(False)
        self.label_12.setTextFormat(Qt.MarkdownText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_for_source_view_label)

        self.horizontalLayout.addWidget(self.frame_source_view)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_formatPrefix.setCurrentIndex(0)
        self.tabWidget_outputs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "ScoreSight", None)
        )
        ___qtablewidgetitem = self.tableWidget_boxes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "Field", None)
        )
        ___qtablewidgetitem1 = self.tableWidget_boxes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Value", None)
        )
        self.toolButton_addBox.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.toolButton_removeBox.setText(
            QCoreApplication.translate("MainWindow", "-", None)
        )
        self.pushButton_makeBox.setText(
            QCoreApplication.translate("MainWindow", "Add to Scene ->", None)
        )
        self.pushButton_removeBox.setText(
            QCoreApplication.translate("MainWindow", "Remove Selected", None)
        )
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Target:", None))
        self.label_selectedInfo.setText(
            QCoreApplication.translate("MainWindow", "Select an item above", None)
        )
        self.pushButton_restoreDefaults.setText(
            QCoreApplication.translate("MainWindow", "Defaults", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Format", None))
        self.comboBox_formatPrefix.setItemText(
            0, QCoreApplication.translate("MainWindow", "Time mm:ss.d", None)
        )
        self.comboBox_formatPrefix.setItemText(
            1, QCoreApplication.translate("MainWindow", "Time mm:ss", None)
        )
        self.comboBox_formatPrefix.setItemText(
            2, QCoreApplication.translate("MainWindow", "Time ss.d", None)
        )
        self.comboBox_formatPrefix.setItemText(
            3, QCoreApplication.translate("MainWindow", "Time 0-59", None)
        )
        self.comboBox_formatPrefix.setItemText(
            4, QCoreApplication.translate("MainWindow", "Shotclock 0-39", None)
        )
        self.comboBox_formatPrefix.setItemText(
            5, QCoreApplication.translate("MainWindow", "Score 1dd", None)
        )
        self.comboBox_formatPrefix.setItemText(
            6, QCoreApplication.translate("MainWindow", "Score ddd", None)
        )
        self.comboBox_formatPrefix.setItemText(
            7, QCoreApplication.translate("MainWindow", "Period 1-4", None)
        )
        self.comboBox_formatPrefix.setItemText(
            8, QCoreApplication.translate("MainWindow", "Period d", None)
        )
        self.comboBox_formatPrefix.setItemText(
            9, QCoreApplication.translate("MainWindow", "Alphanumeric", None)
        )
        self.comboBox_formatPrefix.setItemText(
            10, QCoreApplication.translate("MainWindow", "Any text", None)
        )
        self.comboBox_formatPrefix.setItemText(
            11, QCoreApplication.translate("MainWindow", "Any number", None)
        )
        self.comboBox_formatPrefix.setItemText(
            12, QCoreApplication.translate("MainWindow", "Select Preset", None)
        )

        self.label_13.setText(QCoreApplication.translate("MainWindow", "Type", None))
        self.comboBox_fieldType.setItemText(
            0, QCoreApplication.translate("MainWindow", "Number 0-9", None)
        )
        self.comboBox_fieldType.setItemText(
            1, QCoreApplication.translate("MainWindow", "Time 0-9 , . :", None)
        )
        self.comboBox_fieldType.setItemText(
            2, QCoreApplication.translate("MainWindow", "Text", None)
        )

        self.checkBox_smoothing.setText(
            QCoreApplication.translate("MainWindow", "Average Output", None)
        )
        self.checkBox_ordinalIndicator.setText(
            QCoreApplication.translate("MainWindow", "Ordinal (1st, 2nd, ..)", None)
        )
        self.checkBox_skip_empty.setText(
            QCoreApplication.translate("MainWindow", "Skip Empty Values", None)
        )
        self.checkBox_skip_similar_image.setText(
            QCoreApplication.translate("MainWindow", "Skip Similar Image", None)
        )
        self.checkBox_autocrop.setText(
            QCoreApplication.translate("MainWindow", "Auto Crop", None)
        )
        self.checkBox_invertPatch.setText(
            QCoreApplication.translate("MainWindow", "Invert Input", None)
        )
        self.checkBox_removeLeadingZeros.setText(
            QCoreApplication.translate("MainWindow", "Remove leading 0s", None)
        )
        # if QT_CONFIG(tooltip)
        self.checkBox_dotDetector.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Count dots/blobs instead of detecting characters", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkBox_dotDetector.setText(
            QCoreApplication.translate("MainWindow", "Dot Counter", None)
        )
        # if QT_CONFIG(tooltip)
        self.checkBox_rescalePatch.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Scale the image to 35 pixels height, a favorable size for OCR",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkBox_rescalePatch.setText(
            QCoreApplication.translate("MainWindow", "Rescale Input", None)
        )
        # if QT_CONFIG(tooltip)
        self.checkBox_normWHRatio.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Scale to a favorable 1:2 width-to-height ratio", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkBox_normWHRatio.setText(
            QCoreApplication.translate("MainWindow", "Normalize W-H Ratio", None)
        )
        self.label_binarizationMethod.setText(
            QCoreApplication.translate("MainWindow", "Binarize", None)
        )
        self.comboBox_binarizationMethod.setItemText(
            0, QCoreApplication.translate("MainWindow", "Global", None)
        )
        self.comboBox_binarizationMethod.setItemText(
            1, QCoreApplication.translate("MainWindow", "No Binarization", None)
        )
        self.comboBox_binarizationMethod.setItemText(
            2, QCoreApplication.translate("MainWindow", "Local", None)
        )
        self.comboBox_binarizationMethod.setItemText(
            3, QCoreApplication.translate("MainWindow", "Adaptive", None)
        )

        self.label_4.setText(QCoreApplication.translate("MainWindow", "Cleanup", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", "V.Scale", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Dilate", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "Skew", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Conf. Th", None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "OCR Model", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Folder", None))
        self.pushButton_selectFolder.setText(
            QCoreApplication.translate("MainWindow", "Open", None)
        )
        self.toolButton_trashFolder.setText(
            QCoreApplication.translate("MainWindow", "Clear", None)
        )
        self.checkBox_saveCsv.setText(
            QCoreApplication.translate("MainWindow", "Save .csv file", None)
        )
        self.checkBox_saveXML.setText(
            QCoreApplication.translate("MainWindow", "Save .xml file", None)
        )
        self.label_append.setText(
            QCoreApplication.translate("MainWindow", "Append", None)
        )
        self.comboBox_appendMethod.setItemText(
            0, QCoreApplication.translate("MainWindow", "Results in .csv file", None)
        )
        self.comboBox_appendMethod.setItemText(
            1, QCoreApplication.translate("MainWindow", "Results in .txt files", None)
        )
        self.comboBox_appendMethod.setItemText(
            2, QCoreApplication.translate("MainWindow", "Results in both", None)
        )
        self.comboBox_appendMethod.setItemText(
            3, QCoreApplication.translate("MainWindow", "Don't append results", None)
        )

        # if QT_CONFIG(tooltip)
        self.label_savePerSec.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "How many times per second to save the results to files",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_savePerSec.setText(
            QCoreApplication.translate("MainWindow", "Save / s", None)
        )
        self.tabWidget_outputs.setTabText(
            self.tabWidget_outputs.indexOf(self.tab_textFiles),
            QCoreApplication.translate("MainWindow", "Text Files", None),
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>HTML Scoreboard: <a href="http://localhost:18099/scoresight"><span style=" text-decoration: underline; color:#0000ff;">http://localhost:18099/scoresight<br/></span></a>JSON: <a href="http://localhost:18099/json"><span style=" text-decoration: underline; color:#0000ff;">http://localhost:18099/json</span></a> (optional: ?pivot)<br/>XML: <a href="http://localhost:18099/xml"><span style=" text-decoration: underline; color:#0000ff;">http://localhost:18099/xml</span></a> (optional: ?pivot)<br/>CSV: <a href="http://localhost:18099/csv"><span style=" text-decoration: underline; color:#0000ff;">http://localhost:18099/csv</span></a></p></body></html>',
                None,
            )
        )
        self.tabWidget_outputs.setTabText(
            self.tabWidget_outputs.indexOf(self.tab_browser),
            QCoreApplication.translate("MainWindow", "Browser", None),
        )
        self.pushButton_connectObs.setText(
            QCoreApplication.translate("MainWindow", "Connect OBS", None)
        )
        self.lineEdit_sceneName.setText(
            QCoreApplication.translate("MainWindow", "ScoreSight Scene", None)
        )
        self.pushButton_createOBSScene.setText(
            QCoreApplication.translate("MainWindow", "Create OBS Scene", None)
        )
        self.checkBox_recreate.setText(
            QCoreApplication.translate("MainWindow", "Recreate", None)
        )
        self.tabWidget_outputs.setTabText(
            self.tabWidget_outputs.indexOf(self.tab_obs),
            QCoreApplication.translate("MainWindow", "OBS", None),
        )
        self.connectionLabel.setText(
            QCoreApplication.translate("MainWindow", "Connection", None)
        )
        self.lineEdit_vmixHost.setText(
            QCoreApplication.translate("MainWindow", "localhost", None)
        )
        self.label_5.setText(QCoreApplication.translate("MainWindow", ":", None))
        self.lineEdit_vmixPort.setText(
            QCoreApplication.translate("MainWindow", "8099", None)
        )
        self.pushButton_startvmix.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )
        self.vmixinputLabel.setText(
            QCoreApplication.translate("MainWindow", "Input", None)
        )
        self.inputLineEdit_vmix.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        self.tabWidget_outputs.setTabText(
            self.tabWidget_outputs.indexOf(self.tab_vmix),
            QCoreApplication.translate("MainWindow", "VMix", None),
        )
        self.pushButton_stopUpdates.setText(
            QCoreApplication.translate("MainWindow", "Stop Updates", None)
        )
        self.label_detectionCadence.setText(
            QCoreApplication.translate("MainWindow", "Detections / s", None)
        )
        # if QT_CONFIG(tooltip)
        self.checkBox_updateOnchange.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Only send an update if the field value has changed", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.checkBox_updateOnchange.setText(
            QCoreApplication.translate("MainWindow", "Update on change", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "Source", None))
        self.comboBox_camera_source.setItemText(
            0, QCoreApplication.translate("MainWindow", "Select a source", None)
        )
        self.comboBox_camera_source.setItemText(
            1, QCoreApplication.translate("MainWindow", "Open a Video File", None)
        )
        self.comboBox_camera_source.setItemText(
            2, QCoreApplication.translate("MainWindow", "URL Source (HTTP, RTSP)", None)
        )
        self.comboBox_camera_source.setItemText(
            3, QCoreApplication.translate("MainWindow", "Screen Capture", None)
        )

        # if QT_CONFIG(tooltip)
        self.pushButton_refresh_sources.setToolTip(
            QCoreApplication.translate("MainWindow", "Refresh Sources", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.pushButton_refresh_sources.setText(
            QCoreApplication.translate("MainWindow", "Reload", None)
        )
        self.pushButton_binary.setText(
            QCoreApplication.translate("MainWindow", "Binary View", None)
        )
        self.pushButton_fourCorner.setText(
            QCoreApplication.translate("MainWindow", "4-corner Correction", None)
        )
        # if QT_CONFIG(tooltip)
        self.toolButton_topCrop.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Apply cropping to the entire image", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.toolButton_topCrop.setText(
            QCoreApplication.translate("MainWindow", "Crop", None)
        )
        self.pushButton_stabilize.setText(
            QCoreApplication.translate("MainWindow", "Stabilize", None)
        )
        # if QT_CONFIG(tooltip)
        self.toolButton_osd.setToolTip(
            QCoreApplication.translate("MainWindow", "Show Statistics", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.toolButton_osd.setText(
            QCoreApplication.translate("MainWindow", "OSD", None)
        )
        # if QT_CONFIG(tooltip)
        self.toolButton_showOCRrects.setToolTip(
            QCoreApplication.translate("MainWindow", "Show OCR Detection Boxes", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.toolButton_showOCRrects.setText(
            QCoreApplication.translate("MainWindow", "OCR", None)
        )
        # if QT_CONFIG(tooltip)
        self.toolButton_zoomReset.setToolTip(
            QCoreApplication.translate("MainWindow", "Reset zoom", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.toolButton_zoomReset.setText(
            QCoreApplication.translate("MainWindow", "1:1", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "Ctrl-scroll to zoom", None)
        )
        self.label_16.setText(QCoreApplication.translate("MainWindow", "Left", None))
        self.spinBox_leftCrop.setSuffix(
            QCoreApplication.translate("MainWindow", "px", None)
        )
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Top", None))
        self.spinBox_topCrop.setSuffix(
            QCoreApplication.translate("MainWindow", "px", None)
        )
        self.label_18.setText(QCoreApplication.translate("MainWindow", "Right", None))
        self.spinBox_rightCrop.setSuffix(
            QCoreApplication.translate("MainWindow", "px", None)
        )
        self.label_19.setText(QCoreApplication.translate("MainWindow", "Bottom", None))
        self.spinBox_bottomCrop.setSuffix(
            QCoreApplication.translate("MainWindow", "px", None)
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow", "### Open a Camera or Load a File", None
            )
        )

    # retranslateUi
