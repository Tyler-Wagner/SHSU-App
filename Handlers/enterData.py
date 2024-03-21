from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt, QObject
from datetime import datetime

# Update the add_table_row method in EnterDataHandler
class EnterDataHandler(QObject):
    log_row_added = pyqtSignal(str)
    pAlerts_row_added = pyqtSignal(str)
    cAlerts_row_added = pyqtSignal(str)

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui

    def add_log_row(self, category, message):
        log_entry = f"{category}: {message}"
        self.log_row_added.emit(log_entry)

    def add_past_alerts_row(self, category, message):
        pAlerts_entry = f"{category}: {message}"
        self.pAlerts_row_added.emit(pAlerts_entry)

    def add_current_alerts_row(self, category, message):
        cAlerts_entry = f"{category}: {message}"
        self.cAlerts_row_added.emit(cAlerts_entry)

    def add_table_row(self, log_entry):
        # print(f"Received log data: {log_entry}") #for Debug
        

        # Extract packet and details from log_entry
        # Assuming log_entry has the format "Packet: {packet} -> {details}"
        packet_start = log_entry.find("Packet: ") + len("Packet: ")
        details_start = log_entry.find(" -> ") + len(" -> ")
        packet = log_entry[packet_start:details_start - len(" -> ")]
        details = log_entry[details_start:]

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

    def add_table_row_cAlerts(self, log_entry):
        # print(f"Received log data: {log_entry}") #for Debug
            

        # Extract packet and details from log_entry
        # Assuming log_entry has the format "Packet: {packet} -> {details}"
        packet_start = log_entry.find("Packet: ") + len("Packet: ")
        details_start = log_entry.find(" -> ") + len(" -> ")
        packet = log_entry[packet_start:details_start - len(" -> ")]
        details = log_entry[details_start:]

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
        self.ui.activeAlertsTable.setItem(0, 0, date_item)
        self.ui.activeAlertsTable.setItem(0, 1, time_item)
        self.ui.activeAlertsTable.setItem(0, 2, packet_item)
        self.ui.activeAlertsTable.setItem(0, 3, details_item)

    def add_table_row_pAlerts(self, log_entry):
        # print(f"Received log data: {log_entry}") #for Debug
        

        # Extract packet and details from log_entry
        # Assuming log_entry has the format "Packet: {packet} -> {details}"
        packet_start = log_entry.find("Packet: ") + len("Packet: ")
        details_start = log_entry.find(" -> ") + len(" -> ")
        packet = log_entry[packet_start:details_start - len(" -> ")]
        details = log_entry[details_start:]

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
        self.ui.pastAlertsTable.setItem(0, 0, date_item)
        self.ui.pastAlertsTable.setItem(0, 1, time_item)
        self.ui.pastAlertsTable.setItem(0, 2, packet_item)
        self.ui.pastAlertsTable.setItem(0, 3, details_item)