from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt, QObject
from datetime import datetime

# Update the add_table_row method in EnterDataHandler
class EnterDataHandler(QObject):
    log_row_added = pyqtSignal(str, str)
    pAlerts_row_added = pyqtSignal(str, str, str, str)
    cAlerts_row_added = pyqtSignal(str, str, str)

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui

    def add_log_row(self, category, message):
        self.log_row_added.emit(category, message)

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
        self.ui.logTable.insertRow(0)

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
        self.ui.logTable.setItem(0, 0, date_item)
        self.ui.logTable.setItem(0, 1, time_item)
        self.ui.logTable.setItem(0, 2, packet_item)
        self.ui.logTable.setItem(0, 3, details_item)

    def add_table_row_cAlerts(self, sourceIP, sourceP, destP):
        # print(f"Received log data: {log_entry}") #for Debug
        
        current_datetime = datetime.now()
        dtEntry = current_datetime.strftime("%Y-%m-%d/%H:%M:%S")

        row_count = self.ui.activeAlertsTable.rowCount()
        self.ui.activeAlertsTable.insertRow(row_count)

        # Add items to each cell in the new row
        dateTime_item = QTableWidgetItem(dtEntry)
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
        self.ui.activeAlertsTable.setItem(0, 0, dateTime_item)
        self.ui.activeAlertsTable.setItem(0, 1, sIP_item)
        self.ui.activeAlertsTable.setItem(0, 2, sP_item)
        self.ui.activeAlertsTable.setItem(0, 3, dPort_item)
        

        # Create a button and set it in the row
        button = QPushButton("Add to Past Alerts")
        button.clicked.connect(lambda row=0: self.add_to_past_alerts(row))
        self.ui.activeAlertsTable.setCellWidget(0, 4, button)

    def add_table_row_pAlerts(self, date, sourceIP, sourceP, destP):

        row_count = self.ui.pastAlertsTable.rowCount()
        self.ui.pastAlertsTable.insertRow(row_count)

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
        self.ui.pastAlertsTable.setItem(0, 0, dateTime_item)
        self.ui.pastAlertsTable.setItem(0, 1, sIP_item)
        self.ui.pastAlertsTable.setItem(0, 2, sP_item)
        self.ui.pastAlertsTable.setItem(0, 3, dPort_item)