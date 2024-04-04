import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Handlers.dbHandle import importUserSettings as user
from PyQt5.QtWidgets import *

class Ui_Tabspage(object):
    def setupUi(self, AdvancedPage):
        if AdvancedPage.objectName():
            AdvancedPage.setObjectName(u"AdvancedPage")
        AdvancedPage.resize(1280, 1066)
        self.tabWidget = QTabWidget(AdvancedPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(130, 80, 1386, 846))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar {\n"
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
"	margin-left: 6px;\n"
"    margin-right: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: red;\n"
"    border-bottom: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"	border-width:4px;\n"
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
""
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
"    border-color: red;\n"
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
"    border: 2px solid red; /* Set the border color for the o"
                        "utline of the QTabWidget */\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.logTable = QTableWidget(self.log)
        if (self.logTable.columnCount() < 4):
            self.logTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.logTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.logTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.logTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.logTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.logTable.setObjectName(u"logTable")
        self.logTable.setGeometry(QRect(20, 10, 1341, 731))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTable.sizePolicy().hasHeightForWidth())
        self.logTable.setSizePolicy(sizePolicy)
        self.logTable.setMinimumSize(QSize(760, 0))
        self.logTable.setAutoFillBackground(False)
        self.logTable.setStyleSheet(u" /* LOG PAGE */\n"
"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black;\n"
"	border-top-style:null;\n"
"	border-left-style:null;\n"
"	border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgba(255,0,0,90);\n"
"	color: black;\n"
"}\n"
"")
        self.logTable.setAutoScroll(False)
        self.logTable.setAlternatingRowColors(True)
        self.logTable.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.logTable.setShowGrid(True)
        self.logTable.setCornerButtonEnabled(False)
        self.logTable.setRowCount(0)
        self.logTable.horizontalHeader().setCascadingSectionResizes(False)
        self.logTable.horizontalHeader().setDefaultSectionSize(339)
        self.logTable.horizontalHeader().setHighlightSections(True)
        self.logTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.logTable.verticalHeader().setVisible(False)
        self.logTable.verticalHeader().setCascadingSectionResizes(False)
        self.logTable.verticalHeader().setHighlightSections(True)
        self.logTable.verticalHeader().setProperty("showSortIndicator", False)
        self.logTable.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.log, "")
        self.alerts = QWidget()
        self.alerts.setObjectName(u"alerts")
        self.activeAlertsTable = QTableWidget(self.alerts)
        if (self.activeAlertsTable.columnCount() < 5):
            self.activeAlertsTable.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.activeAlertsTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.activeAlertsTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.activeAlertsTable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.activeAlertsTable.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.activeAlertsTable.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.activeAlertsTable.setObjectName(u"activeAlertsTable")
        self.activeAlertsTable.setGeometry(QRect(20, 80, 1341, 171))
        self.activeAlertsTable.setStyleSheet(u" /* ALERTS PAGE */\n"
"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black; /* Adjust the thickness and color as needed */\n"
"	border-top-style:null;\n"
"	border-left-style:null;\n"
"	border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: rgba(255,0,0,90);\n"
"	color: black;\n"
"}\n"
"")
        self.activeAlertsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.activeAlertsTable.setAutoScroll(False)
        self.activeAlertsTable.setAlternatingRowColors(True)
        self.activeAlertsTable.setCornerButtonEnabled(False)
        self.activeAlertsTable.setRowCount(0)
        self.activeAlertsTable.horizontalHeader().setDefaultSectionSize(267)
        self.activeAlertsTable.verticalHeader().setVisible(False)
        self.label = QLabel(self.alerts)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(520, 50, 351, 21))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.pastAlertsTable = QTableWidget(self.alerts)
        if (self.pastAlertsTable.columnCount() < 4):
            self.pastAlertsTable.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.pastAlertsTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.pastAlertsTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.pastAlertsTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.pastAlertsTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.pastAlertsTable.setObjectName(u"pastAlertsTable")
        self.pastAlertsTable.setGeometry(QRect(20, 350, 1341, 371))
        self.pastAlertsTable.setStyleSheet(u"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black; /* Adjust the thickness and color as needed */\n"
"	border-top-style:null;\n"
"	border-left-style:null;\n"
"	border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"	color: black;\n"
"	text-align: center;\n"
"	background: rgba(128,128,128,60);\n"
"}\n"
"")
        self.pastAlertsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.pastAlertsTable.setAutoScroll(False)
        self.pastAlertsTable.setAlternatingRowColors(True)
        self.pastAlertsTable.setCornerButtonEnabled(False)
        self.pastAlertsTable.setRowCount(0)
        self.pastAlertsTable.horizontalHeader().setDefaultSectionSize(333)
        self.pastAlertsTable.verticalHeader().setVisible(False)
        self.label_2 = QLabel(self.alerts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 300, 351, 21))
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.alerts, "")
        self.action = QWidget()
        self.action.setObjectName(u"action")
        self.pastAlertsTable_2 = QTableWidget(self.action)
        if (self.pastAlertsTable_2.columnCount() < 5):
            self.pastAlertsTable_2.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.pastAlertsTable_2.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.pastAlertsTable_2.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.pastAlertsTable_2.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.pastAlertsTable_2.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.pastAlertsTable_2.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.pastAlertsTable_2.setObjectName(u"pastAlertsTable_2")
        self.pastAlertsTable_2.setGeometry(QRect(20, 40, 1341, 671))
        self.pastAlertsTable_2.setStyleSheet(u"QTableWidget{\n"
"border: 3px outset black;\n"
"}\n"
"QTableWidget:bar{\n"
"border: 3px outset black;\n"
"}\n"
"QHeaderView {\n"
"    border: 2px solid black; /* Adjust the thickness and color as needed */\n"
"	border-top-style:null;\n"
"	border-left-style:null;\n"
"	border-right-style:null;\n"
"}\n"
"QTableWidget::item {\n"
"	color: black;\n"
"	text-align: center;\n"
"	background: rgba(128,128,128,60);\n"
"}\n"
"")
        self.pastAlertsTable_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.pastAlertsTable_2.setAutoScroll(False)
        self.pastAlertsTable_2.setAlternatingRowColors(True)
        self.pastAlertsTable_2.setCornerButtonEnabled(False)
        self.pastAlertsTable_2.setRowCount(0)
        self.pastAlertsTable_2.horizontalHeader().setDefaultSectionSize(333)
        self.pastAlertsTable_2.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.action, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.interfaceSelectionBox = QSpinBox(self.settings)
        self.interfaceSelectionBox.setObjectName(u"interfaceSelectionBox")
        self.interfaceSelectionBox.setGeometry(QRect(540, 260, 42, 22))
        self.interfaceSelectionBox.setValue(user("interface"))
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 260, 151, 21))
        self.label_4 = QLabel(self.settings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(510, 290, 71, 21))
        self.listWidget = QListWidget(self.settings)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(330, 60, 256, 192))
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setLineWidth(2)
        self.frame_2 = QFrame(self.settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(830, 110, 141, 103))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"    background-color: transparent;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    font-weight: bold;\n"
"	font-size: 10pt\n"
"\n"
"}\n"
"")
        self.checkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-weight: bold;\n"
"	font-size: 10pt;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.RightToLeft)
        self.label_8.setStyleSheet(u"font-color: red;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 30, 171, 21))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.label_6 = QLabel(self.settings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(860, 90, 81, 16))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}\n"
"")
        self.tabWidget.addTab(self.settings, "")
        self.dashboardButton = QPushButton(AdvancedPage)
        self.dashboardButton.setObjectName(u"dashboardButton")
        self.dashboardButton.setGeometry(QRect(1400, 980, 131, 51))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.dashboardButton.setFont(font2)
        self.dashboardButton.setStyleSheet(u"QPushButton{\n"
"border: 2px outset black;\n"
"background:red;\n"
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

        self.retranslateUi(AdvancedPage)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(AdvancedPage)
    # setupUi

    def retranslateUi(self, AdvancedPage):
        AdvancedPage.setWindowTitle(QCoreApplication.translate("AdvancedPage", u"Form", None))
        ___qtablewidgetitem = self.logTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdvancedPage", u"Date", None));
        ___qtablewidgetitem1 = self.logTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdvancedPage", u"Time", None));
        ___qtablewidgetitem2 = self.logTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdvancedPage", u"Packet", None));
        ___qtablewidgetitem3 = self.logTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdvancedPage", u"Details", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), QCoreApplication.translate("AdvancedPage", u"Logs", None))
        ___qtablewidgetitem4 = self.activeAlertsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdvancedPage", u"Date/Time", None));
        ___qtablewidgetitem5 = self.activeAlertsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdvancedPage", u"Source IP", None));
        ___qtablewidgetitem6 = self.activeAlertsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdvancedPage", u"Source Port", None));
        ___qtablewidgetitem7 = self.activeAlertsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdvancedPage", u"Destination Port", None));
        ___qtablewidgetitem8 = self.activeAlertsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AdvancedPage", u"Move To Past", None));
        self.label.setText(QCoreApplication.translate("AdvancedPage", u"Active Alerts", None))
        ___qtablewidgetitem9 = self.pastAlertsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AdvancedPage", u"Date/Time", None));
        ___qtablewidgetitem10 = self.pastAlertsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AdvancedPage", u"Source IP", None));
        ___qtablewidgetitem11 = self.pastAlertsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AdvancedPage", u"Source Port", None));
        ___qtablewidgetitem12 = self.pastAlertsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AdvancedPage", u"Destination Port", None));
        self.label_2.setText(QCoreApplication.translate("AdvancedPage", u"Past Alerts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alerts), QCoreApplication.translate("AdvancedPage", u"Alerts", None))
        ___qtablewidgetitem13 = self.pastAlertsTable_2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AdvancedPage", u"Date", None));
        ___qtablewidgetitem14 = self.pastAlertsTable_2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("AdvancedPage", u"Source IP", None));
        ___qtablewidgetitem15 = self.pastAlertsTable_2.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("AdvancedPage", u"Source Port", None));
        ___qtablewidgetitem16 = self.pastAlertsTable_2.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("AdvancedPage", u"Destination Port", None));
        ___qtablewidgetitem17 = self.pastAlertsTable_2.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("AdvancedPage", u"Suggested Actions", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.action), QCoreApplication.translate("AdvancedPage", u"Actions", None))
        self.label_3.setText(QCoreApplication.translate("AdvancedPage", u"<html><head/><body><p><span style=\" font-size:10pt;\">Select Scanning Interface</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AdvancedPage", u"*Defaule Is 4*", None))
        self.label_7.setText(QCoreApplication.translate("AdvancedPage", u"Allow Notifications", None))
        self.checkBox.setText(QCoreApplication.translate("AdvancedPage", u"Yes", None))
        self.checkBox_2.setText(QCoreApplication.translate("AdvancedPage", u"No", None))
        self.label_8.setText(QCoreApplication.translate("AdvancedPage", u"*Default is Yes*", None))
        self.label_5.setText(QCoreApplication.translate("AdvancedPage", u"Scanning Interface Option", None))
        self.label_6.setText(QCoreApplication.translate("AdvancedPage", u"Notifications", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("AdvancedPage", u"Settings", None))
        self.dashboardButton.setText(QCoreApplication.translate("AdvancedPage", u"Back To Dashboard", None))
    # retranslateUi

