import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTabWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from Frontend.tabs import Ui_tabsPage
from Handlers.enterData import EnterDataHandler

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intruwatch")
        self.resize_to_monitor()  # Resize window to fit monitor size

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout to hold dashboard and table
        self.layout = QVBoxLayout(self.central_widget)

        # Advanced Button
        self.advanced_button = QPushButton("Advanced")
        self.advanced_button.setStyleSheet("""
            QPushButton{
                border: 2px outset black;
                background: red;
                color: white;
                font: bold 14pt;
                border-radius: 20px;
                min-width: 200px;  /* Adjust width as needed */
                min-height: 50px;  /* Adjust height as needed */
            }
            QPushButton:pressed{
                border: 2px outset black;
                background: white;
                color: black;
                font: bold 14pt;
            }
        """)
        self.advanced_button.clicked.connect(self.show_tabs_page)
        self.layout.addWidget(self.advanced_button, alignment=Qt.AlignRight)

        # Create the dashboard widget
        self.dashboard_widget = QWidget()
        self.dashboard_layout = QVBoxLayout(self.dashboard_widget)
        self.layout.addWidget(self.dashboard_widget)

        # Create the table widget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Source IP", "Source Port", "Destination IP", "Destination Port"])
        self.dashboard_layout.addWidget(self.table_widget)

        # Back to Dashboard Button
        self.back_to_dashboard_button = QPushButton("Back to Dashboard")
        self.back_to_dashboard_button.setStyleSheet("""
            QPushButton{
                border: 2px outset black;
                background: red;
                color: white;
                font: bold 14pt;
                border-radius: 20px;
                min-width: 200px;  /* Adjust width as needed */
                min-height: 50px;  /* Adjust height as needed */
            }
            QPushButton:pressed{
                border: 2px outset black;
                background: white;
                color: black;
                font: bold 14pt;
            }
        """)
        self.back_to_dashboard_button.clicked.connect(self.show_dashboard)
        self.back_to_dashboard_button.hide()
        self.layout.addWidget(self.back_to_dashboard_button, alignment=Qt.AlignRight)

        # Create the tab widget and add tabs
        self.tab_widget = QTabWidget()
        self.tabs_page = Ui_tabsPage()
        self.tabs_page.setupUi(self.tab_widget)
        self.layout.addWidget(self.tab_widget)
        self.tab_widget.hide()

        # Create the EnterDataHandler instance
        self.data_handler = EnterDataHandler(self.tabs_page)
        self.data_handler.log_row_added.connect(self.add_table_row)

    def resize_to_monitor(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        self.resize(screen_geometry.width(), screen_geometry.height())

    def show_tabs_page(self):
        self.advanced_button.hide()
        self.table_widget.hide()
        self.back_to_dashboard_button.show()
        self.tab_widget.show()

    def show_dashboard(self):
        self.advanced_button.show()
        self.table_widget.show()
        self.back_to_dashboard_button.hide()
        self.tab_widget.hide()

    def add_table_row(self, data):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        for col, item in enumerate(data):
            self.table_widget.setItem(row_position, col, QTableWidgetItem(str(item)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
