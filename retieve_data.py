from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtGui
import sys
import mysql.connector


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'database'
        self.left = 200
        self.top = 100
        self.width = 500
        self.height = 500
        self.icon = 'venv\cowweb.ico'

        self.init__window()

    def init__window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(4)
        self.vbox.addWidget(self.table)

        self.btn = QPushButton('Load', self)
        self.btn.clicked.connect(self.load_data)

        self.vbox.addWidget(self.btn)

        self.setLayout(self.vbox)
        self.show()

    def load_data(self):

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='abc123',
            database='web_on_mind'
        )

        my_cursor = conn.cursor()
        my_cursor.execute('Select * from ps4_tbl')
        result = my_cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row):
                self.table.setItem(row_number, column_number, QTableWidgetItem(data))


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
