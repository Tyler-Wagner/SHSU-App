import psutil
import threading
import sys 
import os
from Handlers.enterData import EnterDataHandler
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Frontend.ui_Dashboard import Ui_Dashboard
from Frontend.Ui_Tabspage import Ui_Tabspage as tabs
from main import list_network_devices, capture_packets
from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS
from Handlers.dbHandle import importPastAlerts as getPastAlerts
from Handlers.enterData import EnterDataHandler as data_handler
from PyQt5.QtWidgets import *
from Frontend.ui_Dashboard import Ui_Dashboard
from Frontend.Ui_Tabspage import Ui_Tabspage as tabs
from Handlers.dbHandle import importPastAlerts as getPastAlerts

app = QApplication([])

class IntruwatchGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Dashboard()
        # self.ui_tabs = tabs()
        self.dashboard_ui_file_path = os.path.join(os.path.dirname(__file__), "Dashboard.ui")
        self.tabs_ui_file_path = os.path.join(os.path.dirname(__file__), "tabs.ui")
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.open_tabs_page)
        # self.ui_tabs.dashboardButton.clicked.connect(self.dashboardButton)  # Connect back to dashboard button
        self.data_handler = EnterDataHandler(self.ui)
        self.data_handler.log_row_added.connect(self.data_handler.add_table_row)
        self.data_handler.pAlerts_row_added.connect(self.data_handler.add_table_row_pAlerts)
        self.data_handler.cAlerts_row_added.connect(self.data_handler.add_table_row_cAlerts)
        self.data_handler.DashTable_row_added.connect(self.data_handler.add_table_row_cAlerts)
    
    def toggle_view(self):
        # Check if the current central widget is the main window
        if isinstance(self.centralWidget(), type(self.ui)):
            # If it is, switch to the tabbed view
            self.load_tabs()
        else:
            # If it's not, switch back to the main window
            self.load_dashboard()
    
    def load_dashboard(self):
        self.ui
        self.setCentralWidget(tabs)
        # Initialize pushButton and connect its clicked signal
        self.pushButton = self.dashboard_ui.findChild(QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.toggle_view)

    def load_tabs(self):
        self.tabs_ui = loadUi(self.tabs_ui_file_path)
        self.setCentralWidget(self.tabs_ui)
        # Connect the 'clicked' signal of the dashboard button to toggle_view
        self.dashboardButton = self.tabs_ui.findChild(QPushButton, "dashboardButton")
        if self.dashboardButton is not None:
            try:
                self.dashboardButton.clicked.disconnect()
            except TypeError:
                pass
            self.dashboardButton.clicked.connect(self.toggle_view)
        else:
            print("dashboardButton not found")
        devices = list_network_devices()
        for device in devices:
            item = QListWidgetItem(device)
            font = QFont()
            font.setBold(True)
            font.setPointSize(10)
            item.setFont(font)
            self.ui_tabs.listWidget.addItem(item)

        self.loadPastAlerts()

    def loadPastAlerts(self):
        out = getPastAlerts()
        print(out)

        for past_alert in out:
            dtEntry, sourceP, sourceIP, destP = past_alert
            self.data_handler.add_table_row_pAlerts_ONSTART(dtEntry, sourceIP, sourceP, destP)

    def back_to_dashboard(self):
        self.setCentralWidget(self.ui)  # Replace 'centralwidget' with the actual central widget name

    def update_gui(self):
        QApplication.processEvents()

# Your other functions remain the same

def main():
    gui = IntruwatchGUI()
    gui.show()
    app.exec_()

if __name__ == "__main__":
    main()
