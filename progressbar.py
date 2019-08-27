from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar
from PyQt5 import QtGui
from time import sleep
import sys


class Root(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Progress Bar'
        self.left = 300
        self.top = 100
        self.width = 400
        self.height = 400
        self.icon = 'venv\cowweb.ico'

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.components()
        self.show()

    def components(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(20, 20, 400, 30)

        btn = QPushButton('Load', self)
        btn.move(150, 80)
        btn.clicked.connect(self.download)

    def download(self):
        completed = 0

        while completed < 100:
            completed += 1
            sleep(0.5)
            self.progressbar.setValue(completed)
            self.progressbar.setTextVisible(False)


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
