from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys
import mysql.connector


class Root(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Spider'
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.icon = 'venv\cowweb.ico'

        self.start_window()

    def start_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.btn = QPushButton('DB Connection')
        self.btn.clicked.connect(self.db_connection)



        self.show()

    def db_connection(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='abc123',
                database='web_on_mind'
            )
            QMessageBox.about(self, 'Connect', 'Connection Success')

        except mysql.connector.Error:
            QMessageBox.about(self, 'Connect', 'Connection Failed')



App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
