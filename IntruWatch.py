import psutil
# import scapy.all as scapy
# from Backedn.tcp_handler import handle_tcp_packet
# from Backedn.udp_handler import handle_udp_packet
import threading
<<<<<<< Updated upstream
from Handlers.enterData import  EnterDataHandler
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QTimer
from Frontend.tabs import Ui_tabsPage
# from time import sleep # FOR SIMULATION
from Backend.main import list_network_devices
from Backend.main import capture_packets
=======
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Frontend.ui_Dashboard import Ui_Dashboard, RealTimeGraph
from Frontend.Ui_Tabspage import Ui_TabsPage
from Handlers.enterData import EnterDataHandler
from main import list_network_devices, capture_packets
from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS
from Handlers.dbHandle import importPastAlerts as getPastAlerts
>>>>>>> Stashed changes

app = QApplication([])

tabsPage = QMainWindow()
ui = Ui_tabsPage()
ui.setupUi(tabsPage)

data_handler = EnterDataHandler(ui)
data_handler.log_row_added.connect(data_handler.add_table_row)


class DataEntryThread(threading.Thread):
    def __init__(self, data_handler):
        threading.Thread.__init__(self)
        self.data_handler = data_handler

    def run(self):
        devices = list(psutil.net_if_addrs().keys())
        
        choice = 1

        if 1 <= choice <= len(devices):
            selected_interface = devices[choice - 1]
            capture_packets(selected_interface, self.data_handler)

# Update the creation and start of DataEntryThread in the main function
data_thread = DataEntryThread(data_handler)
data_thread.start()


def update_gui():
        QApplication.processEvents()

def main():

    global exit_flag

    data_thread = DataEntryThread(data_handler)
    data_thread.start()

    tabsPage.show()

    app.exec_()

if __name__ == "__main__":
     main()
