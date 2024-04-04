from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
import os

class IntruwatchGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dashboard_ui_file_path = os.path.join(os.path.dirname(__file__), "Dashboard.ui")
        self.tabs_ui_file_path = os.path.join(os.path.dirname(__file__), "tabs.ui")
        
        self.load_dashboard()

        self.show()

    def toggle_view(self):
        # Check if the current central widget is the main window
        if isinstance(self.centralWidget(), type(self.dashboard_ui)):
            # If it is, switch to the tabbed view
            self.load_tabs()
        else:
            # If it's not, switch back to the main window
            self.load_dashboard()

    def load_dashboard(self):
        self.dashboard_ui = loadUi(self.dashboard_ui_file_path)
        self.setCentralWidget(self.dashboard_ui)
        # Initialize pushButton and connect its clicked signal
        self.pushButton = self.dashboard_ui.findChild(QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.toggle_view)

    def load_tabs(self):
        self.tabs_ui = loadUi(self.tabs_ui_file_path)
        self.setCentralWidget(self.tabs_ui)
        # Connect the 'clicked' signal of the dashboard button to toggle_view
        self.dashboardButton = self.tabs_ui.findChild(QPushButton, "dashboardButton")
        if self.dashboardButton is not None:
            try:
                self.dashboardButton.clicked.disconnect()
            except TypeError:
                pass
            self.dashboardButton.clicked.connect(self.toggle_view)
        else:
            print("dashboardButton not found")

    def load_graph(self):
        self.graph_ui = loadUi(self.graph_ui_file_path)
        self.setCentralWidget(self.graph_ui)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = IntruwatchGUI()
    sys.exit(app.exec_())
