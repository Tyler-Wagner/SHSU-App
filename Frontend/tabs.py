from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_tabsPage(object):
    def setupUi(self, tabsPage):
        desktop = QtWidgets.QApplication.desktop()  # Get desktop geometry
        screen_rect = desktop.screenGeometry()
        width, height = screen_rect.width(), screen_rect.height()

        tabsPage.setObjectName("tabsPage")
        tabsPage.resize(int(width * 0.8), int(height * 0.8))  # Resize window to 80% of screen size
        tabsPage.setStyleSheet("QMainWindow{\n"
                               "background-color: white;\n"
                               "border-bottom-width: 3px;\n"
                               "border-left-width:3px;\n"
                               "border-right-width: 3px;\n"
                               "border-style: outset; \n"
                               "border-color:white;\n"
                               "}")

        # Create a layout for the entire page
        self.page_layout = QtWidgets.QVBoxLayout(tabsPage)
        self.page_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero to fill the entire window

        # Create the tab widget
        self.tabWidget = QtWidgets.QTabWidget(tabsPage)
        self.tabWidget.setObjectName("tabWidget")
        self.page_layout.addWidget(self.tabWidget)  # Add tab widget to the page layout

        # Add tabs and settings page
        self.log = QtWidgets.QWidget()
        self.alerts = QtWidgets.QWidget()
        self.history = QtWidgets.QWidget()
        self.settings = QtWidgets.QWidget()  # New settings page widget

        self.tabWidget.addTab(self.log, "Logs")
        self.tabWidget.addTab(self.alerts, "Alerts")
        self.tabWidget.addTab(self.history, "History")
        self.tabWidget.addTab(self.settings, "Settings")  # Add settings tab

        # Apply style to tabs to match the color scheme of buttons
        tab_stylesheet = """
            QTabBar::tab {{
                background-color: red;
                color: white;
                border: 2px solid black;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                border-bottom-left-radius: 0px;
                border-bottom-right-radius: 0px;
                min-width: 50ex;
                padding: 2px;
                margin-left: 6px;
                margin-right: 6px;
            }}

            QTabBar::tab:selected {{
                border-color: red;
                border-bottom: 0px;
                border-bottom-left-radius: 0px;
                border-bottom-right-radius: 0px;
                border-width: 4px;
            }}
        """
        self.tabWidget.setStyleSheet(tab_stylesheet)
        self.retranslateUi(tabsPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabsPage)

    def retranslateUi(self, tabsPage):
        _translate = QtCore.QCoreApplication.translate
        tabsPage.setWindowTitle(_translate("tabsPage", "Tabbed Page"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabsPage = QtWidgets.QWidget()
    ui = Ui_tabsPage()
    ui.setupUi(tabsPage)
    tabsPage.show()
    sys.exit(app.exec_())
