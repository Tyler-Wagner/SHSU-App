import psutil
# import scapy.all as scapy
# from Backedn.tcp_handler import handle_tcp_packet
# from Backedn.udp_handler import handle_udp_packet
import threading
from Handlers.enterData import  EnterDataHandler
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QTimer
from Frontend.tabs import Ui_tabsPage
# from time import sleep # FOR SIMULATION
from Backend.main import list_network_devices
from Backend.main import capture_packets

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
