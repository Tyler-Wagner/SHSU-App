from PyQt5 import QtCore, QtGui, QtWidgets
from Handlers.dbHandle import importUserSettings as getUser
from Handlers.dbHandle import updateUserSettings as setUser


class Ui_TabsPage(object):
    def setupUi(self, AdvancedPage):
        AdvancedPage.setObjectName("AdvancedPage")
        AdvancedPage.resize(1600, 900)
        AdvancedPage.setFixedSize(QtCore.QSize(1600, 900))
        self.tabWidget = QtWidgets.QTabWidget(AdvancedPage)
        self.tabWidget.setGeometry(QtCore.QRect(135, 45, 1321, 721))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: white;\n"
"    border: 2px solid #C4C4C3;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    min-width: 50ex;\n"
"    padding: 2px;\n"
"    margin-left: 6px;\n"
"    margin-right: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: black;\n"
"    border-bottom: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-width:4px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"    background-color: white;\n"
"    border-bottom:0px;\n"
"    border-color: black;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabWidget:pane  {\n"
"    border: 2px solid black; /* Set the border color for the content area */\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: white;\n"
"    border: 2px solid #C4C4C3;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    min-width: 50ex;\n"
"    padding: 2px;\n"
"    margin-left: 6px;\n"
"    margin-right: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: black;\n"
"    border-bottom: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-width: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"    background-color: white;\n"
"    border-bottom: 0px;\n"
"    border-color: black;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabWidget:pane {\n"
"    border: 2px solid black; /* Set the border color for the outline of the QTabWidget */\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.logTable = QtWidgets.QTableWidget(self.log)
        self.logTable.setGeometry(QtCore.QRect(10, 10, 1291, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTable.sizePolicy().hasHeightForWidth())
        self.logTable.setSizePolicy(sizePolicy)
        self.logTable.setMinimumSize(QtCore.QSize(760, 0))
        self.logTable.setAutoFillBackground(False)
        self.logTable.setStyleSheet(" /* LOG PAGE */\n"
"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black;\n"
"    border-top-style:null;\n"
"    border-left-style:null;\n"
"    border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgba(0,0,0,90);\n"
"    color: black;\n"
"}\n"
"")
        self.logTable.setAutoScroll(False)
        self.logTable.setAlternatingRowColors(True)
        self.logTable.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.logTable.setShowGrid(True)
        self.logTable.setCornerButtonEnabled(False)
        self.logTable.setRowCount(0)
        self.logTable.setObjectName("logTable")
        self.logTable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.logTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.logTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.logTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.logTable.setHorizontalHeaderItem(3, item)
        self.logTable.horizontalHeader().setCascadingSectionResizes(False)
        self.logTable.horizontalHeader().setDefaultSectionSize(321)
        self.logTable.horizontalHeader().setHighlightSections(True)
        self.logTable.horizontalHeader().setSortIndicatorShown(False)
        self.logTable.verticalHeader().setVisible(False)
        self.logTable.verticalHeader().setCascadingSectionResizes(False)
        self.logTable.verticalHeader().setHighlightSections(True)
        self.logTable.verticalHeader().setSortIndicatorShown(False)
        self.logTable.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.log, "")
        self.alerts = QtWidgets.QWidget()
        self.alerts.setObjectName("alerts")
        self.splitter = QtWidgets.QSplitter(self.alerts)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 1301, 671))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.activeAlertsTable = QtWidgets.QTableWidget(self.splitter)
        self.activeAlertsTable.setStyleSheet(" /* ALERTS PAGE */\n"
"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black; /* Adjust the thickness and color as needed */\n"
"    border-top-style:null;\n"
"    border-left-style:null;\n"
"    border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgba(255,0,0,90);\n"
"    color: black;\n"
"}\n"
"")
        self.activeAlertsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.activeAlertsTable.setAutoScroll(False)
        self.activeAlertsTable.setAlternatingRowColors(True)
        self.activeAlertsTable.setCornerButtonEnabled(False)
        self.activeAlertsTable.setRowCount(0)
        self.activeAlertsTable.setObjectName("activeAlertsTable")
        self.activeAlertsTable.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.activeAlertsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.activeAlertsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.activeAlertsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.activeAlertsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.activeAlertsTable.setHorizontalHeaderItem(4, item)
        self.activeAlertsTable.horizontalHeader().setDefaultSectionSize(259)
        self.activeAlertsTable.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pastAlertsTable = QtWidgets.QTableWidget(self.splitter)
        self.pastAlertsTable.setStyleSheet("QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black; /* Adjust the thickness and color as needed */\n"
"    border-top-style:null;\n"
"    border-left-style:null;\n"
"    border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"    color: black;\n"
"    text-align: center;\n"
"    background: rgba(128,128,128,60);\n"
"}\n"
"")
        self.pastAlertsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.pastAlertsTable.setAutoScroll(False)
        self.pastAlertsTable.setAlternatingRowColors(True)
        self.pastAlertsTable.setCornerButtonEnabled(False)
        self.pastAlertsTable.setRowCount(0)
        self.pastAlertsTable.setObjectName("pastAlertsTable")
        self.pastAlertsTable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.pastAlertsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.pastAlertsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.pastAlertsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.pastAlertsTable.setHorizontalHeaderItem(3, item)
        self.pastAlertsTable.horizontalHeader().setDefaultSectionSize(322)
        self.pastAlertsTable.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.alerts, "")
        self.action = QtWidgets.QWidget()
        self.action.setObjectName("action")
        self.textBrowser = QtWidgets.QTextBrowser(self.action)
        self.textBrowser.setGeometry(QtCore.QRect(280, 20, 901, 191))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    background-color:green;\n"
"    color: white;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.action)
        self.textBrowser_2.setGeometry(QtCore.QRect(280, 230, 901, 191))
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"    background-color:rgb(255, 205, 0);\n"
"    color: black;\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.action)
        self.textBrowser_3.setGeometry(QtCore.QRect(280, 440, 901, 201))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
"    background-color:rgb(185, 0, 0);\n"
"    color: white;\n"
"}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_9 = QtWidgets.QLabel(self.action)
        self.label_9.setGeometry(QtCore.QRect(280, 650, 901, 21))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.action, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.interfaceSelectionBox = QtWidgets.QSpinBox(self.settings)
        self.interfaceSelectionBox.setGeometry(QtCore.QRect(540, 260, 42, 22))
        self.interfaceSelectionBox.setProperty("value", getUser('interface'))
        self.interfaceSelectionBox.setObjectName("interfaceSelectionBox")
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setGeometry(QtCore.QRect(390, 260, 151, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.settings)
        self.label_4.setGeometry(QtCore.QRect(510, 290, 71, 21))
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.settings)
        self.listWidget.setGeometry(QtCore.QRect(330, 60, 256, 192))
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(2)
        self.listWidget.setObjectName("listWidget")
        self.frame_2 = QtWidgets.QFrame(self.settings)
        self.frame_2.setGeometry(QtCore.QRect(830, 110, 141, 103))
        self.interfaceSelectionBox.valueChanged.connect(lambda value: self.updateDatabase_INTERFACE('interface', value)) #PLEASE DO NOT MESS WITH!!

        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setStyleSheet("QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 2, 1)
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    font-weight: bold;\n"
"    font-size: 10pt\n"
"\n"
"}\n"
"")
        self.checkBox.setChecked(getUser('notifications'))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setStyleSheet("QCheckBox {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setChecked(not getUser('notifications'))
        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setStyleSheet("font-color: black;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.settings)
        self.checkBox_2.stateChanged.connect(self.toggleCheckBox1)
        self.checkBox.stateChanged.connect(self.toggleCheckBox2)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 171, 21))
        self.label_5.setStyleSheet("QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.settings)
        self.label_6.setGeometry(QtCore.QRect(860, 90, 81, 16))
        self.label_6.setStyleSheet("QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.settings)
        self.textBrowser_4.setGeometry(QtCore.QRect(490, 360, 441, 131))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget.addTab(self.settings, "")
        self.dashboardButton = QtWidgets.QPushButton(AdvancedPage)
        self.dashboardButton.setGeometry(QtCore.QRect(1340, 820, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.dashboardButton.setFont(font)
        self.dashboardButton.setStyleSheet("QPushButton{\n"
"border: 2px outset black;\n"
"background:blue;\n"
"color: white;\n"
"font: bold 8pt;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px outset black;\n"
"background:white;\n"
"color: black;\n"
"font: bold 8pt;\n"
"}")
        self.dashboardButton.setObjectName("dashboardButton")

        self.retranslateUi(AdvancedPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdvancedPage)
        
        

    def retranslateUi(self, AdvancedPage):
        _translate = QtCore.QCoreApplication.translate
        AdvancedPage.setWindowTitle(_translate("AdvancedPage", "Form"))
        item = self.logTable.horizontalHeaderItem(0)
        item.setText(_translate("AdvancedPage", "Date"))
        item = self.logTable.horizontalHeaderItem(1)
        item.setText(_translate("AdvancedPage", "Time"))
        item = self.logTable.horizontalHeaderItem(2)
        item.setText(_translate("AdvancedPage", "Packet"))
        item = self.logTable.horizontalHeaderItem(3)
        item.setText(_translate("AdvancedPage", "Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("AdvancedPage", "Logs"))
        self.label.setText(_translate("AdvancedPage", "Active Alerts"))
        item = self.activeAlertsTable.horizontalHeaderItem(0)
        item.setText(_translate("AdvancedPage", "Date/Time"))
        item = self.activeAlertsTable.horizontalHeaderItem(1)
        item.setText(_translate("AdvancedPage", "Source IP"))
        item = self.activeAlertsTable.horizontalHeaderItem(2)
        item.setText(_translate("AdvancedPage", "Source Port"))
        item = self.activeAlertsTable.horizontalHeaderItem(3)
        item.setText(_translate("AdvancedPage", "Send To Virus Total"))
        item = self.activeAlertsTable.horizontalHeaderItem(4)
        item.setText(_translate("AdvancedPage", "Move To Past"))
        self.label_2.setText(_translate("AdvancedPage", "Past Alerts"))
        item = self.pastAlertsTable.horizontalHeaderItem(0)
        item.setText(_translate("AdvancedPage", "Date/Time"))
        item = self.pastAlertsTable.horizontalHeaderItem(1)
        item.setText(_translate("AdvancedPage", "Source IP"))
        item = self.pastAlertsTable.horizontalHeaderItem(2)
        item.setText(_translate("AdvancedPage", "Source Port"))
        item = self.pastAlertsTable.horizontalHeaderItem(3)
        item.setText(_translate("AdvancedPage", "Destination Port"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alerts), _translate("AdvancedPage", "Alerts"))
        self.textBrowser.setHtml(_translate("AdvancedPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">If you feel the threat is LOW Level:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">        Inital Investigation:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Analyze the network traffic or system logs associated with the alert.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Check for any signs of suspicious activity or anomalies.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Consult additional security tools or resources if necessary.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        </span><span style=\" font-size:11pt; font-weight:600;\">Response:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">    </span><span style=\" font-size:11pt;\">If the alert is confirmed to be a false positive, diregard the alert and move it to the past alerts table.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    If there\'s evidence of a security threat, implement any necessary mitigations or countermeasures to address the threat.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("AdvancedPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">If you feel the threat is MEDIUM Level:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">        Inital Investigation:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Review the alert details promptly to understand the potential threat.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        </span><span style=\" font-size:11pt; font-weight:600;\">Response:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Conduct a thorough analysis of the network or system logs associated with the alert.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Look for indicators of compromise (IOCs) and any potential security breaches.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Take immediate action to contain the threat and prevent further damage.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Isolate affected systems and block malicious IP addresses.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("AdvancedPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">If you feel the threat is HIGH Level:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">        Immediate Response:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Contain the threat and prevent further damage or compromise.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Isolate affected systems or segments of the network to stop the spread of the attack.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Conduct a detailed forensic analysis of the affected systems to understand the extent of the breach.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">        </span><span style=\" font-size:11pt; font-weight:600;\">Recovery:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Work towards restoring normal operations while ensuring that the security posture is strengthened to prevent similar </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    incidents in the future.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">    Implement comprehensive security measures.</span></p></body></html>"))
        self.label_9.setText(_translate("AdvancedPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">**Please read the Disclaimer on the settings page.**</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.action), _translate("AdvancedPage", "Actions"))
        self.label_3.setText(_translate("AdvancedPage", "<html><head/><body><p><span style=\" font-size:10pt;\">Select Scanning Interface</span></p></body></html>"))
        self.label_4.setText(_translate("AdvancedPage", "*Defaule Is 4*"))
        self.label_7.setText(_translate("AdvancedPage", "Allow Notifications"))
        self.checkBox.setText(_translate("AdvancedPage", "Yes"))
        self.checkBox_2.setText(_translate("AdvancedPage", "No"))
        self.label_8.setText(_translate("AdvancedPage", "*Default is Yes*"))
        self.label_5.setText(_translate("AdvancedPage", "Scanning Interface Option"))
        self.label_6.setText(_translate("AdvancedPage", "Notifications"))
        self.textBrowser_4.setHtml(_translate("AdvancedPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Disclaimer: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">We operate as an Intrusion Detection System (IDS) and do not possess decision-making capabilities on behalf of users. Our primary function is to detect and alert users about potential security breaches or anomalies within the system. While we provide valuable insights, it is ultimately the responsibility of users to interpret and act upon the information provided by the IDS.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("AdvancedPage", "Settings"))
        self.dashboardButton.setText(_translate("AdvancedPage", "Back To Dashboard"))

    def toggleCheckBox1(self, state):
        if state == QtCore.Qt.Checked:
            self.checkBox.setChecked(False)
        else:
            self.checkBox.setChecked(True)
        setUser('notifications', 'F')

    def toggleCheckBox2(self, state):
        if state == QtCore.Qt.Checked:
            self.checkBox_2.setChecked(False)
        else:
            self.checkBox_2.setChecked(True)
        setUser('notifications', 'T')

                

    def updateDatabase_INTERFACE(self, table, info):
        setUser(table, info)
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AdvancedPage = QtWidgets.QWidget()
#     ui = Ui_AdvancedPage()
#     ui.setupUi(AdvancedPage)
#     AdvancedPage.show()
#     sys.exit(app.exec_())