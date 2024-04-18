import psutil
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Frontend.Ui_Dashboard import Ui_Dashboard, RealTimeGraph
from Frontend.Ui_Tabspage import Ui_TabsPage
from Handlers.enterData import EnterDataHandler
from Backend.main import capture_packets
from Handlers.dbHandle import importUserSettings as dbhandle_SETTINGS
from Handlers.dbHandle import importPastAlerts as getPastAlerts
from Handlers.sendNotification import sendnotification
from Handlers.dbHandle import clearCounterDB, checkDate, updateDate, updateCount, setDate, setFirstRun, getFirstRun, updateFirstRun
from Frontend.Ui_vTotalReturn import Ui_Form
from datetime import datetime

app = QApplication([])
app.setAttribute(Qt.AA_EnableHighDpiScaling, True)

DashPage = QMainWindow()
Dash_ui = Ui_Dashboard()
Dash_ui.setupUi(DashPage)

TabsPage = QWidget()
tabs_ui = Ui_TabsPage()
tabs_ui.setupUi(TabsPage)

vTotalPage = QWidget()
vTotal_ui=Ui_Form() 
vTotal_ui.setupUi(vTotalPage)

# Instantiate the EnterDataHandler class with references to UI objects
data_handler = EnterDataHandler(Dash_ui, tabs_ui, vTotal_ui, DashPage, TabsPage, vTotalPage)
data_handler.log_row_added.connect(data_handler.add_table_row) # connects to the log table
data_handler.pAlerts_row_added.connect(data_handler.add_table_row_pAlerts) # connects to the Past Alerts Table
data_handler.cAlerts_row_added.connect(data_handler.add_table_row_cAlerts) # connects to the Current Alerts Table
data_handler.tableWidgetle_row_added.connect(data_handler.tableWidgetRow)
data_handler.pastcount_updated.connect(Dash_ui.update_past_alerts_count)
data_handler.currentCount_updated.connect(Dash_ui.update_current_alerts_count)

real_time_graph = RealTimeGraph()
real_time_graph.setFixedSize(1381, 471)
real_time_graph.setGeometry(QRect( 10, 92, 1381, 471))

if not Dash_ui.centralwidget.layout():
    layout = QVBoxLayout(Dash_ui.centralwidget)
else:
    layout = Dash_ui.centralwidget.layout()

# Add a stretch item to create empty space above the graph widget
layout.addStretch(2)

# Add real-time graph to the central widget layout
layout.addWidget(real_time_graph)

# Add another stretch item to create empty space below the graph widget
layout.addStretch(10)

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
    
    for past_alert in out:
        # Extract the necessary information from the past_alert tuple
        dtEntry, sourceP, sourceIP, destP = past_alert  # Adjust the order of arguments if needed

        # Add the past alert to the data handler
        data_handler.add_table_row_pAlerts_ONSTART(dtEntry, sourceIP, sourceP, destP)  # Pass the arguments correctly

    pass
def showDash():
    TabsPage.hide()
    DashPage.show()
    pass
def showTabs():
    DashPage.hide()
    TabsPage.show()
    pass
def closeVTotal():
    vTotalPage.close()
    TabsPage.show()
    pass
def main():
    DashPage.show()
    clearCounterDB()
    
    #Button setup
    data_thread = DataEntryThread(data_handler)
    data_thread.start()
    advanced_button = DashPage.findChild(QPushButton, "pushButton")
    dashboard_button = TabsPage.findChild(QPushButton, "dashboardButton")
    vTotalButton = vTotalPage.findChild(QPushButton, "closeButton")
    advanced_button.clicked.connect(lambda: showTabs())
    dashboard_button.clicked.connect(lambda: showDash())
    vTotalButton.clicked.connect(lambda: closeVTotal())
    #gen Device list
    devices = list_network_devices()
    for device in devices:
        item = QListWidgetItem(device)
        # Create a QFont object for bold text with 10pt size
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)  # Set the point size to 10
        item.setFont(font)
        tabs_ui.listWidget.addItem(item)
    loadPastAlerts()
    
    #Check api Date and reset counter if needed
    date = datetime.now()
    currentDate = date.strftime("%Y-%m-%d")
    
    if checkDate() == None:
        setDate(currentDate)
    if currentDate != checkDate():
        updateCount(1000)
        updateDate(currentDate)
        updateCount(1000)
        
    if getFirstRun == None:
        #IF THERE IS NO DATA SET TO TRUE
        setFirstRun()
    if getFirstRun() == 1:
        #TODO
        #RUN WIZ 
        updateFirstRun()# sets First run to 0

    data_thread.start()
    #### TEST ATTACK########################################
    data_handler.add_current_alerts_row('123456789', 22,22)
    sendnotification("TEST ATTACK", f"Source IP: 123456789 Source port: 22 Dest port: 22")
    #### TEST ATTACK########################################
    
    app.exec_()

if __name__ == "__main__":
     main()
