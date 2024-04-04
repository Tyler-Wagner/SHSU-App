import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from random import randint
from typing import Optional
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class RealTimeGraph(QWidget):
    def __init__(self, chart_title: Optional[str] = None, histo_tick_size: int = 200):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.fig, self.ax = plt.subplots()
        self.ax.set_title(chart_title)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amount of Packets")
        self.ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: datetime.utcfromtimestamp(x).strftime('%H:%M:%S')))
        self.TCP_dataset, = self.ax.plot([], [], label="TCP")
        self.UDP_dataset, = self.ax.plot([], [], label="UDP")
        self.ICMP_dataset, = self.ax.plot([], [], label="ICMP")
        self.ax.legend()
        self.TCP_data = []
        self.UDP_data = []
        self.ICMP_data = []
        self.dates = []
        self.animation = FuncAnimation(self.fig, self.update, interval=1000)

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def update(self, frame):
        date_px = datetime.now().timestamp()
        self.dates.append(date_px)
        self.TCP_data.append(randint(5,1000))
        self.UDP_data.append(randint(0,250))
        self.ICMP_data.append(randint(1,75))

        self.TCP_dataset.set_data(self.dates, self.TCP_data)
        self.UDP_dataset.set_data(self.dates, self.UDP_data)
        self.ICMP_dataset.set_data(self.dates, self.ICMP_data)

        # Set Y-axis limits dynamically based on the maximum values of the data
        max_value = max(max(self.TCP_data), max(self.UDP_data), max(self.ICMP_data))
        self.ax.set_ylim(0, max_value + 5)  # Add some margin for better visualization

        self.ax.relim()
        self.ax.autoscale_view(True,True,True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Graph")
        self.setGeometry(100, 100, 800, 600)

        central_widget = RealTimeGraph(chart_title="Packet Graph")
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
