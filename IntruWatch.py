import psutil
import threading
from Handlers.enterData import  EnterDataHandler
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtGui import QFont
from Frontend.ui_Dashboard import Ui_Dashboard as IntruwatchGUI
from Frontend.Ui_Tabspage import Ui_Tabspage as tabs
from main import list_network_devices, capture_packets
from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS
from Handlers.dbHandle import importPastAlerts as getPastAlerts

app = QApplication([])
Dashboard = QMainWindow()
tabsPage = QListWidgetItem()
ui_Dashboard = IntruwatchGUI()
ui_tabs = tabs()
ui_tabs.setupUi(tabsPage)

data_handler = EnterDataHandler(ui_tabs)
data_handler.log_row_added.connect(data_handler.add_table_row) # connects to the log table
data_handler.pAlerts_row_added.connect(data_handler.add_table_row_pAlerts) # connects to the Past Alerts Table
data_handler.cAlerts_row_added.connect(data_handler.add_table_row_cAlerts) # connects to the Current Alerts Table

class DataEntryThread(threading.Thread):
    def __init__(self, data_handler):
        threading.Thread.__init__(self)
        self.data_handler = data_handler

    def run(self):
        devices = list(psutil.net_if_addrs().keys())
        
        choice = dbhandle_SETTINGS('interface')

        if 1 <= choice <= len(devices):
            selected_interface = devices[choice - 1]
            capture_packets(selected_interface, self.data_handler)

# Update the creation and start of DataEntryThread in the main function
data_thread = DataEntryThread(data_handler)
data_thread.start()


def update_gui():
    QApplication.processEvents()

def list_network_devices():
    devices = psutil.net_if_addrs()
    device_list = []
    i=1
    for name, addresses in devices.items():
        device_list.append(f"{i}: {name}")
        i+=1
    return device_list

def loadPastAlerts():
    out = getPastAlerts()
    print(out)
    
    for past_alert in out:
        # Extract the necessary information from the past_alert tuple
        dtEntry, sourceP, sourceIP, destP = past_alert  # Adjust the order of arguments if needed

        # Add the past alert to the data handler
        data_handler.add_table_row_pAlerts_ONSTART(dtEntry, sourceIP, sourceP, destP)  # Pass the arguments correctly

    pass

def main():

    data_thread = DataEntryThread(data_handler)
    data_thread.start()
    
    Dashboard.show()
    tabs.show
    devices = list_network_devices()
    for device in devices:
        item = QListWidgetItem(device)
        # Create a QFont object for bold text with 10pt size
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)  # Set the point size to 10
        item.setFont(font)
        ui_tabs.listWidget.addItem(item)
    loadPastAlerts()

    app.exec_()

if __name__ == "__main__":
     main()
