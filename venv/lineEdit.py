from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
import sys


class Root(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Hubble'
        self.left = 300
        self.top = 200
        self.width = 300
        self.height = 400
        self.icon = 'cowweb.ico'

        self.start_window()

    def start_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        self.show()

    def create_layout(self):
        hbox_layout = QHBoxLayout()

        self.entrybox1 = QLineEdit(self)
        #entrybox1.setGeometry(QRect(100,100,200,20))
        self.entrybox1.setFont(QtGui.QFont('Arial', 10))
        hbox_layout.addWidget(self.entrybox1)


        btn1 = QPushButton('Find', self)
        btn1.setFont(QtGui.QFont('Arial', 10))
        btn1.clicked.connect(self.click)
        hbox_layout.addWidget(btn1)

        self.lbl1 = QLabel()
        self.lbl1.setFont(QtGui.QFont('Calibri', 10))
        hbox_layout.addWidget(self.lbl1)

        self.setLayout(hbox_layout)

    def click(self):
        self.lbl1.setText(self.entrybox1.text())


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
