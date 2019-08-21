from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys


class Root(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window properties.
        self.title = 'Hubble'
        self.top = 100
        self.left = 300
        self.width = 500
        self.height = 500
        self.icon = 'cowweb.ico'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.UIComponents()
        self.show()

    def UIComponents(self):
        """
        Creating a button for user interface
        - setting button size and position
        - adding an icon
        - setting the icon
        - adding a tooltip
        - simple event handle function click
        """
        button = QPushButton('Search', self)
        button.setGeometry(QRect(100,100,200,50))
        button.setIcon(QtGui.QIcon(self.icon))
        button.setIconSize(QtCore.QSize(20,20))
        button.setToolTip('<h3>Start Searching the web catalog</h3>')
        #button.clicked.connect(self.click)



# Creating window instance and running in a loop.
App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
