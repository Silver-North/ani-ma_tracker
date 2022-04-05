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
        MainWindow.resize(397, 178)
        MainWindow.setMinimumSize(QtCore.QSize(397, 178))
        MainWindow.setMaximumSize(QtCore.QSize(397, 178))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(367, 4, 25, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_11 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_11.setGeometry(QtCore.QRect(367, 34, 25, 25))
        self.toolButton_11.setObjectName("toolButton_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 361, 181))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.toolButton_2.setGeometry(QtCore.QRect(330, 29, 25, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 29, 85, 26))
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(4, 29, 233, 26))
        self.comboBox.setObjectName("comboBox")
        self.toolButton_5 = QtWidgets.QToolButton(self.tab)
        self.toolButton_5.setGeometry(QtCore.QRect(182, 60, 41, 41))
        self.toolButton_5.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(300, 1, 25, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_4 = QtWidgets.QToolButton(self.tab)
        self.toolButton_4.setGeometry(QtCore.QRect(138, 60, 41, 41))
        self.toolButton_4.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_7 = QtWidgets.QToolButton(self.tab)
        self.toolButton_7.setGeometry(QtCore.QRect(314, 60, 41, 41))
        self.toolButton_7.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_7.setObjectName("toolButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(4, 1, 233, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(240, 1, 55, 27))
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.toolButton_8 = QtWidgets.QToolButton(self.tab)
        self.toolButton_8.setGeometry(QtCore.QRect(314, 105, 41, 41))
        self.toolButton_8.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.tab)
        self.toolButton_9.setGeometry(QtCore.QRect(270, 60, 41, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon3)
        self.toolButton_9.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_12 = QtWidgets.QToolButton(self.tab)
        self.toolButton_12.setGeometry(QtCore.QRect(226, 60, 41, 41))
        self.toolButton_12.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_10 = QtWidgets.QToolButton(self.tab)
        self.toolButton_10.setGeometry(QtCore.QRect(330, 1, 25, 25))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_16 = QtWidgets.QToolButton(self.tab)
        self.toolButton_16.setGeometry(QtCore.QRect(270, 105, 41, 41))
        self.toolButton_16.setStatusTip("")
        self.toolButton_16.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_16.setObjectName("toolButton_16")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(4, 58, 130, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setGeometry(QtCore.QRect(4, 84, 130, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(4, 110, 219, 31))
        self.comboBox_7.setCurrentText("")
        self.comboBox_7.setFrame(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.toolButton_33 = QtWidgets.QToolButton(self.tab)
        self.toolButton_33.setGeometry(QtCore.QRect(241, 113, 25, 25))
        self.toolButton_33.setIcon(icon2)
        self.toolButton_33.setObjectName("toolButton_33")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(225, 118, 14, 14))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolButton_13 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_13.setGeometry(QtCore.QRect(314, 100, 41, 41))
        self.toolButton_13.setStatusTip("")
        self.toolButton_13.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_15 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_15.setGeometry(QtCore.QRect(326, 5, 25, 25))
        self.toolButton_15.setStatusTip("")
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_17 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_17.setGeometry(QtCore.QRect(267, 100, 41, 41))
        self.toolButton_17.setStatusTip("")
        self.toolButton_17.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_17.setObjectName("toolButton_17")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(236, 5, 81, 27))
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox.setSpecialValueText("")
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setSuffix("")
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(6, 100, 101, 41))
        self.lcdNumber_2.setDigitCount(8)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.toolButton_19 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_19.setGeometry(QtCore.QRect(236, 36, 25, 25))
        self.toolButton_19.setStatusTip("")
        self.toolButton_19.setObjectName("toolButton_19")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(6, 36, 221, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.toolButton_20 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_20.setGeometry(QtCore.QRect(220, 100, 41, 41))
        self.toolButton_20.setStatusTip("")
        self.toolButton_20.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_20.setObjectName("toolButton_20")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(109, 100, 101, 41))
        self.lcdNumber_3.setDigitCount(8)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.toolButton_21 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_21.setGeometry(QtCore.QRect(266, 36, 25, 25))
        self.toolButton_21.setStatusTip("")
        self.toolButton_21.setObjectName("toolButton_21")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(6, 5, 221, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_14 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_14.setGeometry(QtCore.QRect(326, 36, 25, 25))
        self.toolButton_14.setStatusTip("")
        self.toolButton_14.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_14.setObjectName("toolButton_14")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setGeometry(QtCore.QRect(6, 70, 345, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_5.setGeometry(QtCore.QRect(109, 100, 101, 41))
        self.lcdNumber_5.setDigitCount(8)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.toolButton_27 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_27.setGeometry(QtCore.QRect(314, 100, 41, 41))
        self.toolButton_27.setStatusTip("")
        self.toolButton_27.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_27.setObjectName("toolButton_27")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab_5)
        self.lcdNumber_4.setGeometry(QtCore.QRect(6, 100, 101, 41))
        self.lcdNumber_4.setDigitCount(8)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.toolButton_26 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_26.setGeometry(QtCore.QRect(220, 100, 41, 41))
        self.toolButton_26.setStatusTip("")
        self.toolButton_26.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_26.setObjectName("toolButton_26")
        self.toolButton_31 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_31.setGeometry(QtCore.QRect(267, 100, 41, 41))
        self.toolButton_31.setStatusTip("")
        self.toolButton_31.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_31.setObjectName("toolButton_31")
        self.toolButton_28 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_28.setGeometry(QtCore.QRect(326, 36, 25, 25))
        self.toolButton_28.setStatusTip("")
        self.toolButton_28.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_28.setObjectName("toolButton_28")
        self.toolButton_29 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_29.setGeometry(QtCore.QRect(236, 36, 25, 25))
        self.toolButton_29.setStatusTip("")
        self.toolButton_29.setObjectName("toolButton_29")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(6, 5, 221, 26))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_6.setGeometry(QtCore.QRect(6, 36, 221, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.tab_5)
        self.progressBar_7.setGeometry(QtCore.QRect(6, 70, 345, 23))
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName("progressBar_7")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(236, 5, 81, 27))
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox_2.setSpecialValueText("")
        self.doubleSpinBox_2.setPrefix("")
        self.doubleSpinBox_2.setSuffix("")
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setMaximum(9999.99)
        self.doubleSpinBox_2.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_2.setProperty("value", 0.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.toolButton_32 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_32.setGeometry(QtCore.QRect(326, 5, 25, 25))
        self.toolButton_32.setStatusTip("")
        self.toolButton_32.setObjectName("toolButton_32")
        self.toolButton_30 = QtWidgets.QToolButton(self.tab_5)
        self.toolButton_30.setGeometry(QtCore.QRect(266, 36, 25, 25))
        self.toolButton_30.setStatusTip("")
        self.toolButton_30.setObjectName("toolButton_30")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 2, 231, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(18, 31, 90, 110))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(123, 30, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textEdit.setFont(font)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.toolButton_22 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_22.setGeometry(QtCore.QRect(330, 2, 25, 25))
        self.toolButton_22.setObjectName("toolButton_22")
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar_4.setGeometry(QtCore.QRect(244, 2, 81, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(123, 30, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setMarkdown("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(18, 31, 90, 110))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 2, 231, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.toolButton_23 = QtWidgets.QToolButton(self.tab_4)
        self.toolButton_23.setGeometry(QtCore.QRect(330, 2, 25, 25))
        self.toolButton_23.setObjectName("toolButton_23")
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_5.setGeometry(QtCore.QRect(244, 2, 81, 23))
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 2, 231, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.toolButton_25 = QtWidgets.QToolButton(self.tab_6)
        self.toolButton_25.setGeometry(QtCore.QRect(330, 2, 25, 25))
        self.toolButton_25.setObjectName("toolButton_25")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(18, 31, 90, 110))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_3.setGeometry(QtCore.QRect(123, 30, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setMarkdown("")
        self.textEdit_3.setObjectName("textEdit_3")
        self.progressBar_6 = QtWidgets.QProgressBar(self.tab_6)
        self.progressBar_6.setGeometry(QtCore.QRect(244, 2, 81, 23))
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.toolButton_18 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_18.setGeometry(QtCore.QRect(367, 64, 25, 25))
        self.toolButton_18.setObjectName("toolButton_18")
        self.toolButton_24 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_24.setGeometry(QtCore.QRect(367, 152, 25, 25))
        self.toolButton_24.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(367, 94, 25, 25))
        self.toolButton_6.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_6.setObjectName("toolButton_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ani-Ma checker"))
        self.toolButton_3.setToolTip(_translate("MainWindow", "Close"))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.comboBox.setToolTip(_translate("MainWindow", "Current Checker List"))
        self.toolButton_5.setToolTip(_translate("MainWindow", "One"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setToolTip(_translate("MainWindow", "All"))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.toolButton_7.setToolTip(_translate("MainWindow", "Log Info"))
        self.toolButton_7.setText(_translate("MainWindow", "..."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Write URL:"))
        self.spinBox.setToolTip(_translate("MainWindow", "Series"))
        self.toolButton_8.setToolTip(_translate("MainWindow", "Download Info"))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.toolButton_9.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_9.setText(_translate("MainWindow", "..."))
        self.toolButton_12.setToolTip(_translate("MainWindow", "Checking.."))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.toolButton_10.setToolTip(_translate("MainWindow", "Notify"))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Open URL"))
        self.toolButton_16.setText(_translate("MainWindow", "..."))
        self.progressBar.setToolTip(_translate("MainWindow", "Progress Download file.."))
        self.progressBar_2.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.comboBox_7.setToolTip(_translate("MainWindow", "Current Tracker List"))
        self.toolButton_33.setToolTip(_translate("MainWindow", "Save urk from Track"))
        self.toolButton_33.setText(_translate("MainWindow", "..."))
        self.checkBox.setToolTip(_translate("MainWindow", "Toggle open Track link"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Anime"))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Log"))
        self.toolButton_13.setText(_translate("MainWindow", "..."))
        self.toolButton_15.setToolTip(_translate("MainWindow", "Saved"))
        self.toolButton_15.setText(_translate("MainWindow", "..."))
        self.toolButton_17.setToolTip(_translate("MainWindow", "Check.."))
        self.toolButton_17.setText(_translate("MainWindow", "..."))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "Numbers"))
        self.lcdNumber_2.setToolTip(_translate("MainWindow", "Readed"))
        self.toolButton_19.setToolTip(_translate("MainWindow", "Deleted"))
        self.toolButton_19.setText(_translate("MainWindow", "..."))
        self.toolButton_20.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_20.setText(_translate("MainWindow", "..."))
        self.lcdNumber_3.setToolTip(_translate("MainWindow", "Current"))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Edit Readed"))
        self.toolButton_21.setText(_translate("MainWindow", "..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Write URL"))
        self.toolButton_14.setToolTip(_translate("MainWindow", "Open URL"))
        self.toolButton_14.setText(_translate("MainWindow", "..."))
        self.progressBar_3.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Manga"))
        self.lcdNumber_5.setToolTip(_translate("MainWindow", "Current"))
        self.toolButton_27.setToolTip(_translate("MainWindow", "Log"))
        self.toolButton_27.setText(_translate("MainWindow", "..."))
        self.lcdNumber_4.setToolTip(_translate("MainWindow", "Readed"))
        self.toolButton_26.setToolTip(_translate("MainWindow", "Update"))
        self.toolButton_26.setText(_translate("MainWindow", "..."))
        self.toolButton_31.setToolTip(_translate("MainWindow", "Check.."))
        self.toolButton_31.setText(_translate("MainWindow", "..."))
        self.toolButton_28.setToolTip(_translate("MainWindow", "Open URL"))
        self.toolButton_28.setText(_translate("MainWindow", "..."))
        self.toolButton_29.setToolTip(_translate("MainWindow", "Deleted"))
        self.toolButton_29.setText(_translate("MainWindow", "..."))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Write URL"))
        self.progressBar_7.setToolTip(_translate("MainWindow", "Progress Checking.."))
        self.doubleSpinBox_2.setToolTip(_translate("MainWindow", "Tom & Chapter"))
        self.toolButton_32.setToolTip(_translate("MainWindow", "Saved"))
        self.toolButton_32.setText(_translate("MainWindow", "..."))
        self.toolButton_30.setToolTip(_translate("MainWindow", "Edit Readed"))
        self.toolButton_30.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Ranobe"))
        self.label_5.setText(_translate("MainWindow", "IMG"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Description..."))
        self.toolButton_22.setToolTip(_translate("MainWindow", "Update Description"))
        self.toolButton_22.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Anime Description"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Description..."))
        self.label_6.setText(_translate("MainWindow", "IMG"))
        self.toolButton_23.setToolTip(_translate("MainWindow", "Update Description"))
        self.toolButton_23.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Manga Description"))
        self.toolButton_25.setToolTip(_translate("MainWindow", "Update Description"))
        self.toolButton_25.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "IMG"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Description..."))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Ranobe Description"))
        self.toolButton_18.setToolTip(_translate("MainWindow", "Hide window"))
        self.toolButton_18.setText(_translate("MainWindow", "..."))
        self.toolButton_24.setToolTip(_translate("MainWindow", "About"))
        self.toolButton_24.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setToolTip(_translate("MainWindow", "Close Connect"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
