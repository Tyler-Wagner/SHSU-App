import psutil
import threading
from Handlers.enterData import  EnterDataHandler
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtGui import QFont
from Frontend.tabs import Ui_tabsPage
from Backend.main import list_network_devices, capture_packets
from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS

app = QApplication([])

tabsPage = QMainWindow()
ui = Ui_tabsPage()
ui.setupUi(tabsPage)

data_handler = EnterDataHandler(ui)
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

def main():

    data_thread = DataEntryThread(data_handler)
    data_thread.start()

    tabsPage.show()
    devices = list_network_devices()
    for device in devices:
        item = QListWidgetItem(device)
        # Create a QFont object for bold text with 10pt size
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)  # Set the point size to 10
        item.setFont(font)
        ui.listWidget.addItem(item)

    app.exec_()

if __name__ == "__main__":
     main()
