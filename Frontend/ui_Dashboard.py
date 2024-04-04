import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1182, 887)
        Dashboard.setAutoFillBackground(False)
        Dashboard.setStyleSheet(u"color:rgb(255,0,0);")
        Dashboard.setAnimated(True)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(980, 810, 131, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 2px outset black;\n"
"background:red;\n"
"color: white;\n"
"font: bold 14pt;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 2px outset black;\n"
"background:white;\n"
"color: black;\n"
"font: bold 14pt;\n"
"}")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(960, 10, 151, 121))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:red;\n"
"color: white;\n"
"font: bold 8pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_2)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_4)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:red;\n"
"color: white;\n"
"font: bold 8pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_3)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setFont(font2)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(11, 11, 901, 61))
        font3 = QFont()
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel{\n"
"border: 2px outset black;\n"
"background:red;\n"
"color: white;\n"
"font: bold 36pt;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 79, 901, 291))
        self.frame.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border : 2px outsetblack;\n"
"font: bold 14pt;\n"
"border-radius: 15px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Graph = QLabel(self.frame)
        self.Graph.setObjectName(u"Graph")
        self.Graph.setPixmap(QPixmap(u"Generic.png"))
        self.Graph.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Graph)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 128):
            self.tableWidget.setRowCount(128)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 380, 901, 421))
        self.tableWidget.setStyleSheet(u"\n"
"border: 2px outset black;\n"
"background:white;\n"
"color: black;\n"
"font: bold 14pt;\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(128)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(219)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Intruwatch Dash", None))
        self.pushButton.setText(QCoreApplication.translate("Dashboard", u"Advanced", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Packets Scanned", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"PSCounter", None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Threats Detected", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"TDCounter", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Intruwatch Dashboard", None))
        self.Graph.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Source IP", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Source Port", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"Destination IP", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"Destination Port", None));
    # retranslateUi

