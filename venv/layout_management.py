from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys


class Root(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Spider'
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.icon = 'cowweb.ico'

        self.start_window()

    def start_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)

        self.show()

    def create_layout(self):
        self.groupbox = QGroupBox("What do you want from our spidy?")
        hboxlayout = QHBoxLayout()

        button1 = QPushButton('Camera', self)
        button1.setGeometry(QRect(100,100,150,50))
        button1.setIcon(QtGui.QIcon(self.icon))
        button1.setIconSize(QtCore.QSize(20,30))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton('Games', self)
        button2.setGeometry(QRect(100,100,150,50))
        button2.setIcon(QtGui.QIcon(self.icon))
        button2.setIconSize(QtCore.QSize(20,30))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        button3 = QPushButton('Shirts', self)
        button3.setGeometry(QRect(100,100,150,50))
        button3.setIcon(QtGui.QIcon(self.icon))
        button3.setIconSize(QtCore.QSize(20,30))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button3)

        self.groupbox.setLayout(hboxlayout)



App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
