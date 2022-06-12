# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parser.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 178)
        MainWindow.setMinimumSize(QtCore.QSize(390, 178))
        MainWindow.setMaximumSize(QtCore.QSize(390, 178))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(364, -1, 25, 25))
        self.toolButton_3.setStyleSheet("border: none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_11.setGeometry(QtCore.QRect(364, 69, 25, 25))
        self.toolButton_11.setObjectName("toolButton_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 361, 181))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.toolButton_2.setGeometry(QtCore.QRect(314, 29, 41, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(19, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(226, 29, 85, 26))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(2, 29, 221, 26))
        self.comboBox.setObjectName("comboBox")
        self.toolButton_5 = QtWidgets.QToolButton(self.tab)
        self.toolButton_5.setGeometry(QtCore.QRect(226, 58, 41, 41))
        self.toolButton_5.setToolTip("")
        self.toolButton_5.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(314, 1, 41, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(19, 19))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(2, 1, 309, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton_8 = QtWidgets.QToolButton(self.tab)
        self.toolButton_8.setGeometry(QtCore.QRect(314, 106, 41, 41))
        self.toolButton_8.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_12 = QtWidgets.QToolButton(self.tab)
        self.toolButton_12.setGeometry(QtCore.QRect(270, 58, 41, 41))
        self.toolButton_12.setToolTip("")
        self.toolButton_12.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_12.setObjectName("toolButton_12")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(2, 58, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setGeometry(QtCore.QRect(2, 79, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(2, 113, 221, 25))
        self.comboBox_7.setCurrentText("")
        self.comboBox_7.setFrame(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(226, 112, 14, 14))
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(41, 49))
        self.checkBox.setAutoRepeatDelay(300)
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(226, 60, 41, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 41, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(-5, 103, 391, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.toolButton_16 = QtWidgets.QToolButton(self.frame)
        self.toolButton_16.setGeometry(QtCore.QRect(290, 10, 26, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_16.setFont(font)
        self.toolButton_16.setStyleSheet("border: none")
        self.toolButton_16.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/checkbox-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon3)
        self.toolButton_16.setIconSize(QtCore.QSize(53, 35))
        self.toolButton_16.setObjectName("toolButton_16")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(275, 10, 14, 14))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(275, 25, 14, 14))
        self.checkBox_4.setText("")
        self.checkBox_4.setIconSize(QtCore.QSize(41, 49))
        self.checkBox_4.setAutoRepeatDelay(300)
        self.checkBox_4.setObjectName("checkBox_4")
        self.toolButton_9 = QtWidgets.QToolButton(self.frame)
        self.toolButton_9.setGeometry(QtCore.QRect(290, 25, 26, 14))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.toolButton_9.setFont(font)
        self.toolButton_9.setStyleSheet("border: none")
        self.toolButton_9.setIconSize(QtCore.QSize(35, 53))
        self.toolButton_9.setObjectName("toolButton_9")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(226, 127, 14, 14))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.tab)
        self.toolButton_4.setGeometry(QtCore.QRect(241, 112, 26, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("border: none")
        self.toolButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/checkbox-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setIconSize(QtCore.QSize(53, 35))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_7 = QtWidgets.QToolButton(self.tab)
        self.toolButton_7.setGeometry(QtCore.QRect(241, 127, 26, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setStyleSheet("border: none")
        self.toolButton_7.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/checkbox-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon5)
        self.toolButton_7.setIconSize(QtCore.QSize(35, 53))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_14 = QtWidgets.QToolButton(self.tab)
        self.toolButton_14.setGeometry(QtCore.QRect(314, 60, 41, 41))
        self.toolButton_14.setStyleSheet("")
        self.toolButton_14.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_14.setObjectName("toolButton_14")
        self.dockWidget = QtWidgets.QDockWidget(self.tab)
        self.dockWidget.setGeometry(QtCore.QRect(0, 70, 164, 80))
        self.dockWidget.setFloating(True)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.comboBox_5 = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_5.setGeometry(QtCore.QRect(2, 4, 79, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_8.setGeometry(QtCore.QRect(83, 4, 79, 26))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(2, 32, 79, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(83, 32, 79, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.dockWidget.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.toolButton_2.raise_()
        self.lcdNumber.raise_()
        self.comboBox.raise_()
        self.toolButton_5.raise_()
        self.toolButton.raise_()
        self.lineEdit.raise_()
        self.toolButton_8.raise_()
        self.toolButton_12.raise_()
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.comboBox_7.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.toolButton_4.raise_()
        self.toolButton_7.raise_()
        self.toolButton_14.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolButton_13 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_13.setGeometry(QtCore.QRect(314, 105, 41, 41))
        self.toolButton_13.setStatusTip("")
        self.toolButton_13.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_15 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_15.setGeometry(QtCore.QRect(330, 36, 25, 25))
        self.toolButton_15.setStatusTip("")
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_17 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_17.setGeometry(QtCore.QRect(270, 105, 41, 41))
        self.toolButton_17.setStatusTip("")
        self.toolButton_17.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_17.setObjectName("toolButton_17")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(2, 105, 109, 41))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_2.setDigitCount(8)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.toolButton_19 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_19.setGeometry(QtCore.QRect(276, 36, 25, 25))
        self.toolButton_19.setStatusTip("")
        self.toolButton_19.setObjectName("toolButton_19")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(2, 36, 272, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.toolButton_20 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_20.setGeometry(QtCore.QRect(226, 105, 41, 41))
        self.toolButton_20.setStatusTip("")
        self.toolButton_20.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_20.setObjectName("toolButton_20")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(114, 105, 109, 41))
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_3.setDigitCount(8)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.toolButton_21 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_21.setGeometry(QtCore.QRect(303, 36, 25, 25))
        self.toolButton_21.setStatusTip("")
        self.toolButton_21.setObjectName("toolButton_21")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(2, 5, 353, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setGeometry(QtCore.QRect(2, 66, 353, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar_3.setFont(font)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(226, 105, 41, 41))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(270, 105, 41, 41))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_8.raise_()
        self.label_9.raise_()
        self.toolButton_13.raise_()
        self.toolButton_15.raise_()
        self.toolButton_17.raise_()
        self.lcdNumber_2.raise_()
        self.toolButton_19.raise_()
        self.comboBox_2.raise_()
        self.toolButton_20.raise_()
        self.lcdNumber_3.raise_()
        self.toolButton_21.raise_()
        self.lineEdit_2.raise_()
        self.progressBar_3.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.toolButton_27 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_27.setGeometry(QtCore.QRect(314, 105, 41, 41))
        self.toolButton_27.setStatusTip("")
        self.toolButton_27.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_27.setObjectName("toolButton_27")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_4.setGeometry(QtCore.QRect(2, 105, 75, 41))
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber_4.setDigitCount(8)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.toolButton_26 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_26.setGeometry(QtCore.QRect(230, 105, 41, 41))
        self.toolButton_26.setStatusTip("")
        self.toolButton_26.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_26.setObjectName("toolButton_26")
        self.toolButton_31 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_31.setGeometry(QtCore.QRect(272, 105, 41, 41))
        self.toolButton_31.setStatusTip("")
        self.toolButton_31.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_31.setObjectName("toolButton_31")
        self.toolButton_29 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_29.setGeometry(QtCore.QRect(276, 36, 25, 25))
        self.toolButton_29.setStatusTip("")
        self.toolButton_29.setObjectName("toolButton_29")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(2, 5, 353, 26))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_6.setGeometry(QtCore.QRect(2, 36, 272, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.tab_5)
        self.progressBar_7.setGeometry(QtCore.QRect(2, 66, 353, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar_7.setFont(font)
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName("progressBar_7")
        self.toolButton_32 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_32.setGeometry(QtCore.QRect(330, 36, 25, 25))
        self.toolButton_32.setStatusTip("")
        self.toolButton_32.setObjectName("toolButton_32")
        self.toolButton_30 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_30.setGeometry(QtCore.QRect(303, 36, 25, 25))
        self.toolButton_30.setStatusTip("")
        self.toolButton_30.setObjectName("toolButton_30")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_5.setGeometry(QtCore.QRect(78, 105, 75, 41))
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_5.setDigitCount(8)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_6.setGeometry(QtCore.QRect(154, 105, 75, 41))
        self.lcdNumber_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_6.setMidLineWidth(0)
        self.lcdNumber_6.setSmallDecimalPoint(False)
        self.lcdNumber_6.setDigitCount(8)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setProperty("value", 0.0)
        self.lcdNumber_6.setProperty("intValue", 0)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(230, 105, 41, 41))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(272, 105, 41, 41))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_10.raise_()
        self.label_11.raise_()
        self.toolButton_27.raise_()
        self.lcdNumber_4.raise_()
        self.toolButton_26.raise_()
        self.toolButton_31.raise_()
        self.toolButton_29.raise_()
        self.lineEdit_3.raise_()
        self.comboBox_6.raise_()
        self.progressBar_7.raise_()
        self.toolButton_32.raise_()
        self.toolButton_30.raise_()
        self.lcdNumber_5.raise_()
        self.lcdNumber_6.raise_()
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(97, 2, 257, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(4, 31, 90, 110))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(97, 30, 257, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textEdit.setFont(font)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(4, 2, 90, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMaxVisibleItems(20)
        self.comboBox_4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.toolButton_18 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_18.setGeometry(QtCore.QRect(364, 22, 25, 25))
        self.toolButton_18.setIconSize(QtCore.QSize(23, 23))
        self.toolButton_18.setObjectName("toolButton_18")
        self.toolButton_24 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_24.setGeometry(QtCore.QRect(364, 154, 25, 25))
        self.toolButton_24.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(364, 48, 25, 25))
        self.toolButton_6.setIconSize(QtCore.QSize(19, 19))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_10 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_10.setGeometry(QtCore.QRect(364, 88, 25, 25))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_25 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_25.setGeometry(QtCore.QRect(364, 109, 25, 25))
        self.toolButton_25.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_25.setObjectName("toolButton_25")
        self.dockWidget_4 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_4.setGeometry(QtCore.QRect(10, 0, 370, 211))
        self.dockWidget_4.setFocusPolicy(QtCore.Qt.NoFocus)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/bell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dockWidget_4.setWindowIcon(icon6)
        self.dockWidget_4.setFloating(True)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_4)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 370, 191))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        self.dockWidget_2 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_2.setGeometry(QtCore.QRect(220, 80, 171, 91))
        self.dockWidget_2.setFloating(True)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.dockWidgetContents_2)
        self.spinBox_2.setGeometry(QtCore.QRect(2, 10, 80, 27))
        self.spinBox_2.setMaximum(99999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.dockWidgetContents_2)
        self.spinBox_3.setGeometry(QtCore.QRect(86, 10, 80, 27))
        self.spinBox_3.setMaximum(99999999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton_3.setGeometry(QtCore.QRect(2, 40, 164, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.toolButton_3.raise_()
        self.toolButton_18.raise_()
        self.toolButton_24.raise_()
        self.toolButton_11.raise_()
        self.toolButton_10.raise_()
        self.toolButton_6.raise_()
        self.toolButton_25.raise_()
        self.dockWidget_4.raise_()
        self.tabWidget.raise_()
        self.dockWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.comboBox_4.setCurrentIndex(0)
        self.listWidget.setCurrentRow(-1)
        self.toolButton_4.clicked.connect(self.checkBox.click) # type: ignore
        self.toolButton_7.clicked.connect(self.checkBox_2.click) # type: ignore
        self.toolButton_16.clicked.connect(self.checkBox_3.toggle) # type: ignore
        self.toolButton_9.clicked.connect(self.checkBox_4.toggle) # type: ignore
        self.pushButton_2.clicked.connect(self.dockWidget.close) # type: ignore
        self.toolButton_25.clicked.connect(self.dockWidget.show) # type: ignore
        self.toolButton_21.clicked.connect(self.dockWidget_2.show) # type: ignore
        self.toolButton_30.clicked.connect(self.dockWidget_2.show) # type: ignore
        self.pushButton_3.clicked.connect(self.dockWidget_2.close) # type: ignore
        self.toolButton_15.clicked.connect(self.dockWidget_2.show) # type: ignore
        self.toolButton_32.clicked.connect(self.dockWidget_2.show) # type: ignore
        self.toolButton.clicked.connect(self.dockWidget_2.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ani-Ma tracker"))
        self.toolButton_3.setToolTip(_translate("MainWindow", "Close"))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.lcdNumber.setToolTip(_translate("MainWindow", "Current series"))
        self.comboBox.setToolTip(_translate("MainWindow", "Current Tracker List"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Write URL:"))
        self.toolButton_8.setToolTip(_translate("MainWindow", "Log file"))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.progressBar.setToolTip(_translate("MainWindow", "Progress Download file.."))
        self.progressBar_2.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.comboBox_7.setToolTip(_translate("MainWindow", "Current Checker List"))
        self.checkBox.setToolTip(_translate("MainWindow", "Checking mode"))
        self.label_2.setText(_translate("MainWindow", "Q"))
        self.label_3.setText(_translate("MainWindow", "Q"))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Track & Update"))
        self.checkBox_3.setToolTip(_translate("MainWindow", "Tracker mode"))
        self.checkBox_4.setToolTip(_translate("MainWindow", "Format mode"))
        self.toolButton_9.setToolTip(_translate("MainWindow", "Downloading: SD & HD"))
        self.toolButton_9.setText(_translate("MainWindow", "HD | SD"))
        self.checkBox_2.setToolTip(_translate("MainWindow", "Download mode"))
        self.toolButton_4.setToolTip(_translate("MainWindow", "Checking: Save & Open"))
        self.toolButton_7.setToolTip(_translate("MainWindow", "Downloading: All & One"))
        self.toolButton_14.setToolTip(_translate("MainWindow", "MPV player"))
        self.toolButton_14.setText(_translate("MainWindow", "..."))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "       Export History"))
        self.comboBox_5.setToolTip(_translate("MainWindow", "List export"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "anime"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "manga"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "ranobe"))
        self.comboBox_8.setToolTip(_translate("MainWindow", "Format export"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "md"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "txt"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "json"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "xlsx"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Anime"))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Log"))
        self.toolButton_13.setText(_translate("MainWindow", "..."))
        self.toolButton_15.setToolTip(_translate("MainWindow", "Saved"))
        self.toolButton_15.setText(_translate("MainWindow", "..."))
        self.toolButton_17.setToolTip(_translate("MainWindow", "Check.."))
        self.toolButton_17.setText(_translate("MainWindow", "..."))
        self.lcdNumber_2.setToolTip(_translate("MainWindow", "Readed"))
        self.toolButton_19.setToolTip(_translate("MainWindow", "Deleted"))
        self.toolButton_19.setText(_translate("MainWindow", "..."))
        self.toolButton_20.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_20.setText(_translate("MainWindow", "..."))
        self.lcdNumber_3.setToolTip(_translate("MainWindow", "Current"))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Edit Readed"))
        self.toolButton_21.setText(_translate("MainWindow", "..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Write URL"))
        self.progressBar_3.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.label_8.setText(_translate("MainWindow", "Q"))
        self.label_9.setText(_translate("MainWindow", "Q"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Manga"))
        self.toolButton_27.setToolTip(_translate("MainWindow", "Log"))
        self.toolButton_27.setText(_translate("MainWindow", "..."))
        self.lcdNumber_4.setToolTip(_translate("MainWindow", "Readed"))
        self.toolButton_26.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_26.setText(_translate("MainWindow", "..."))
        self.toolButton_31.setToolTip(_translate("MainWindow", "Check.."))
        self.toolButton_31.setText(_translate("MainWindow", "..."))
        self.toolButton_29.setToolTip(_translate("MainWindow", "Deleted"))
        self.toolButton_29.setText(_translate("MainWindow", "..."))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Write URL"))
        self.progressBar_7.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.toolButton_32.setToolTip(_translate("MainWindow", "Saved"))
        self.toolButton_32.setText(_translate("MainWindow", "..."))
        self.toolButton_30.setToolTip(_translate("MainWindow", "Edit Readed"))
        self.toolButton_30.setText(_translate("MainWindow", "..."))
        self.lcdNumber_5.setToolTip(_translate("MainWindow", "Accessing"))
        self.lcdNumber_6.setToolTip(_translate("MainWindow", "Accessing"))
        self.label_10.setText(_translate("MainWindow", "Q"))
        self.label_11.setText(_translate("MainWindow", "Q"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Ranobe"))
        self.label_5.setText(_translate("MainWindow", "IMG"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Description..."))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "anime"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "manga"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ranobe"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Anime Description"))
        self.toolButton_18.setToolTip(_translate("MainWindow", "Open URL"))
        self.toolButton_18.setText(_translate("MainWindow", "..."))
        self.toolButton_24.setToolTip(_translate("MainWindow", "About"))
        self.toolButton_24.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setToolTip(_translate("MainWindow", "Close Connect"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.toolButton_10.setToolTip(_translate("MainWindow", "Notify"))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.toolButton_25.setToolTip(_translate("MainWindow", "Export History"))
        self.toolButton_25.setText(_translate("MainWindow", "..."))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "Notifications"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Editing chapters"))
        self.spinBox_2.setToolTip(_translate("MainWindow", "Chapters"))
        self.spinBox_3.setToolTip(_translate("MainWindow", "Sub Chapters"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Editing count readed chapters"))
        self.pushButton_3.setText(_translate("MainWindow", "Save chapter"))
