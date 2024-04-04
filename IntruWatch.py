import psutil
import threading
import sys
from Handlers.enterData import  EnterDataHandler
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from Frontend.Dashboard import IntruwatchGUI as Dashboard
#from Frontend.Ui_Tabspage import Ui_Tabspage
from main import list_network_devices, capture_packets
#from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS

app = QApplication([])

#tabsPage = QWidget()
#ui = Ui_Tabspage()
#ui.setupUi(tabsPage)

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
        
        #choice = dbhandle_SETTINGS('interface')
        choice = 1
        # if 1 <= choice <= len(devices):
        selected_interface = devices[choice - 1]
        capture_packets(selected_interface)

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
    app = QApplication(sys.argv)
    window = Dashboard()  # Create an instance of Dashboard
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()