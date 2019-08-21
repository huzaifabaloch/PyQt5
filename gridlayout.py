from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QVBoxLayout, QGroupBox, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys


class Root(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Grid Layout'
        self.left = 500
        self.top = 300
        self.width = 400
        self.height = 200
        self.icon = "cowweb.ico"
        self.group_box = ''

        self.start_window()

    def start_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        v_box = QVBoxLayout()
        v_box.addWidget(self.group_box)
        self.setLayout(v_box)
        self.show()

    def create_layout(self):
        self.group_box = QGroupBox('What do you like to have?')
        grid_layout = QGridLayout()

        btn1 = QPushButton('Hiking', self)
        btn1.setGeometry(QRect(20, 20, 50, 50))
        btn1.setIcon(QtGui.QIcon(self.icon))
        btn1.setIconSize(QtCore.QSize(20, 20))
        grid_layout.addWidget(btn1, 0, 0)

        btn2 = QPushButton('Paragliding', self)
        btn2.setGeometry(QRect(20, 20, 50, 50))
        btn2.setIcon(QtGui.QIcon(self.icon))
        btn2.setIconSize(QtCore.QSize(20, 20))
        grid_layout.addWidget(btn2, 0, 1)

        btn3 = QPushButton('Swimming', self)
        btn3.setGeometry(QRect(20, 20, 50, 50))
        btn3.setIcon(QtGui.QIcon(self.icon))
        btn3.setIconSize(QtCore.QSize(20, 20))
        grid_layout.addWidget(btn3, 1, 0)

        btn4 = QPushButton('Horse Riding', self)
        btn4.setGeometry(QRect(20, 20, 50, 50))
        btn4.setIcon(QtGui.QIcon(self.icon))
        btn4.setIconSize(QtCore.QSize(20, 20))
        grid_layout.addWidget(btn4, 1, 1)

        self.group_box.setLayout(grid_layout)


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())



