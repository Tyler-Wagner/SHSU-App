import sys
from PyQt5.QtWidgets import QApplication
from Frontend.Dashboard import Dashboard
from Frontend.tabs import Ui_tabsPage
def main():
    app = QApplication(sys.argv)
    window = Dashboard()  # Create an instance of Dashboard
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()