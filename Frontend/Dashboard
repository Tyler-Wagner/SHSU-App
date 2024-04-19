import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QDesktopWidget, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intruwatch")  # Set the window title

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a label and add it to the layout
        label = QLabel("Dashboard", self)
        label.setStyleSheet("font-size: 20px;")
        layout.addWidget(label)

        # Create the counters and add them to the layout
        self.scanned_packets_counter = QLabel("Scanned Packets: 0", self)
        self.scanned_packets_counter.setStyleSheet("font-size: 12px;")
        layout.addWidget(self.scanned_packets_counter)

        self.threats_detected_counter = QLabel("Threats Detected: 0", self)
        self.threats_detected_counter.setStyleSheet("font-size: 12px;")
        layout.addWidget(self.threats_detected_counter)

        # Create the table and add it to the layout
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Destination IP", "Destination Port", "Source IP", "Source Port"])
        layout.addWidget(self.table)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scale_table(0.6, 0.4)

    def scale_table(self, width_ratio, height_ratio):
        table_width = int(self.width() * width_ratio)
        table_height = int(self.height() * height_ratio)
        self.table.setGeometry(5, self.height() - table_height - 5, table_width - 10, table_height - 10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
