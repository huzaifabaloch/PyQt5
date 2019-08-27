from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QDialog, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'webspider'
        self.left = 200
        self.top = 100
        self.width = 700
        self.height = 500
        self.icon = 'cowweb.ico'

        self.init_window()


    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setFixedWidth(400)
        #self.setFixedHeight(400)
        self.components()
        self.show()


    def components(self):

        vbox = QVBoxLayout()

        lbl1 = QLabel('Email: ', self)
        lbl1.setFont(QtGui.QFont('Arial', 10))
        vbox.addWidget(lbl1)

        lbl2 = QLabel('Password: ', self)
        lbl2.setFont(QtGui.QFont('Arial', 10))
        vbox.addWidget(lbl2)

        entrybox1 = QLineEdit(self)
        entrybox2 = QLineEdit(self)
        entrybox1.setFont(QtGui.QFont('Arial', 10))
        entrybox2.setFont(QtGui.QFont('Arial', 10))

        vbox.addWidget(entrybox1)
        vbox.addWidget(entrybox2)

        self.setLayout(vbox)




App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())

