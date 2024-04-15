from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import pyqtSignal, Qt, QObject
from datetime import datetime
from Handlers.dbHandle import updatePastAlerts as dbhandeler

counter = 0

# Update the add_table_row method in EnterDataHandler
class EnterDataHandler(QObject):
    log_row_added = pyqtSignal(str, str)
    pAlerts_row_added = pyqtSignal(str, str, int, str)
    cAlerts_row_added = pyqtSignal(str, int, int)
    tableWidgetle_row_added = pyqtSignal(str, int, int)


    def __init__(self, dash_ui, tabs_ui, parent=None):
        super().__init__(parent)
        self.dash_ui = dash_ui
        self.tabs_ui = tabs_ui

    def add_log_row(self, category, message):
        self.log_row_added.emit(category, message)

    def add_tableWidgetle_row(self, sourceIP, sourceP, destP):
        self.tableWidgetle_row_added.emit(sourceIP, sourceP, destP)

    def add_past_alerts_row(self, date, sourceIP, sourceP, destP):
        self.pAlerts_row_added.emit(date, sourceIP, sourceP, destP)

    def add_current_alerts_row(self, sourceIP, sourceP, destP):
        self.cAlerts_row_added.emit(sourceIP, sourceP, destP)

    def add_table_row(self, packet, details):
        
        # print(f"Received log data: {log_entry}") #for Debug

        current_datetime = datetime.now()
        date = current_datetime.strftime("%Y-%m-%d")
        time = current_datetime.strftime("%H:%M:%S")

        # Insert a new row at the beginning
        self.tabs_ui.logTable.insertRow(0)

        # Add items to each cell in the new row
        date_item = QTableWidgetItem(date)
        time_item = QTableWidgetItem(time)
        packet_item = QTableWidgetItem(packet)
        details_item = QTableWidgetItem(details)

        # Set font and alignment for each item
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        for item in [date_item, time_item, packet_item, details_item]:
            item.setFont(font)
            item.setTextAlignment(Qt.AlignCenter)

        # Set items in the new row
        self.tabs_ui.logTable.setItem(0, 0, date_item)
        self.tabs_ui.logTable.setItem(0, 1, time_item)
        self.tabs_ui.logTable.setItem(0, 2, packet_item)
        self.tabs_ui.logTable.setItem(0, 3, details_item)

    def tableWidgetRow(self, sourceIP, sourceP, destP):
        global counter
        # print(f"Received log data: {log_entry}") #for Debug
        if counter != 100:
            counter += 1
        else:
            current_datetime = datetime.now()
            dtEntry = current_datetime.strftime("%H:%M:%S")

            self.dash_ui.tableWidget.insertRow(0)

            # Add items to each cell in the new row
            dateTime_item = QTableWidgetItem(dtEntry)
            sIP_item = QTableWidgetItem(sourceIP)
            if sourceP == -1 or destP == -1:
                sP_item = QTableWidgetItem("N/A")
                dPort_item = QTableWidgetItem("N/A")
            else:
                sP_item = QTableWidgetItem(str(sourceP))
                dPort_item = QTableWidgetItem(str(destP))
            
            # Set font and alignment for each item
            font = QFont()
            font.setPointSize(14)
            font.setBold(True)

            for item in [dateTime_item, sIP_item, sP_item, dPort_item]:
                item.setFont(font)
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(QColor('red'))

            # Set items in the new row
            self.dash_ui.tableWidget.setItem(0, 0, dateTime_item)
            self.dash_ui.tableWidget.setItem(0, 1, sIP_item)
            self.dash_ui.tableWidget.setItem(0, 2, sP_item)
            self.dash_ui.tableWidget.setItem(0, 3, dPort_item)
            counter = 1
        

    def add_table_row_cAlerts(self, sourceIP, sourceP, destP):
        # print(f"Received log data: {log_entry}") #for Debug
        
        current_datetime = datetime.now()
        dtEntry = current_datetime.strftime("%Y-%m-%d/%H:%M:%S")

        self.tabs_ui.activeAlertsTable.insertRow(0)

        # Add items to each cell in the new row
        dateTime_item = QTableWidgetItem(dtEntry)
        sIP_item = QTableWidgetItem(sourceIP)
        sP_item = QTableWidgetItem(str(sourceP))
        dPort_item = QTableWidgetItem(str(destP))

        # Set font and alignment for each item
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        for item in [dateTime_item, sIP_item, sP_item, dPort_item]:
            item.setFont(font)
            item.setTextAlignment(Qt.AlignCenter)

        # Set items in the new row
        self.tabs_ui.activeAlertsTable.setItem(0, 0, dateTime_item)
        self.tabs_ui.activeAlertsTable.setItem(0, 1, sIP_item)
        self.tabs_ui.activeAlertsTable.setItem(0, 2, sP_item)
        self.tabs_ui.activeAlertsTable.setItem(0, 3, dPort_item)
        

        # Create a button and set it in the row
        button = QPushButton("Add to Past Alerts")
        button.clicked.connect(lambda: self.add_table_row_pAlerts(dtEntry, sourceIP, str(sourceP), str(destP)))
        self.tabs_ui.activeAlertsTable.setCellWidget(0, 4, button)

    def add_table_row_pAlerts(self, date, sourceIP, sourceP, destP):
        dbhandeler(date, sourceIP, sourceP, destP)
        
        #Finding and removeing the Row in cAlerts Table
        row_count = self.tabs_ui.activeAlertsTable.rowCount()
        for i in range(row_count):
            if self.tabs_ui.activeAlertsTable.item(i, 0).text() == date:
                # Remove the row from CAlerts
                self.tabs_ui.activeAlertsTable.removeRow(i)
                break
        
        self.tabs_ui.pastAlertsTable.insertRow(0)

        # Add items to each cell in the new row
        dateTime_item = QTableWidgetItem(date)
        sIP_item = QTableWidgetItem(sourceIP)
        sP_item = QTableWidgetItem(sourceP)
        dPort_item = QTableWidgetItem(destP)

        # Set font and alignment for each item
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        for item in [dateTime_item, sIP_item, sP_item, dPort_item]:
            item.setFont(font)
            item.setTextAlignment(Qt.AlignCenter)

        # Set items in the new row
        self.tabs_ui.pastAlertsTable.setItem(0, 0, dateTime_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 1, sIP_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 2, sP_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 3, dPort_item)
    
    def add_table_row_pAlerts_ONSTART(self, date, sourceIP, sourceP, destP):
        # dbhandeler(date, sourceIP, sourceP, destP)
        
        #Finding and removeing the Row in cAlerts Table
        row_count = self.tabs_ui.activeAlertsTable.rowCount()
        for i in range(row_count):
            if self.tabs_ui.activeAlertsTable.item(i, 0).text() == date:
                # Remove the row from CAlerts
                self.tabs_ui.activeAlertsTable.removeRow(i)
                break
        
        self.tabs_ui.pastAlertsTable.insertRow(0)

        # Add items to each cell in the new row
        dateTime_item = QTableWidgetItem(date)
        sIP_item = QTableWidgetItem(sourceIP)
        sP_item = QTableWidgetItem(sourceP)
        dPort_item = QTableWidgetItem(destP)

        # Set font and alignment for each item
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)

        for item in [dateTime_item, sIP_item, sP_item, dPort_item]:
            item.setFont(font)
            item.setTextAlignment(Qt.AlignCenter)

        # Set items in the new row
        self.tabs_ui.pastAlertsTable.setItem(0, 0, dateTime_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 1, sIP_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 2, sP_item)
        self.tabs_ui.pastAlertsTable.setItem(0, 3, dPort_item)