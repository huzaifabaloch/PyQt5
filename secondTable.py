from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Second(QDialog):
    def __init__(self, record):
        super().__init__()

        self.title = 'second'
        self.left = 400
        self.top = 100
        self.width = 800
        self.height = 500
        self.icon = 'venv\cowweb.ico'
        self.record = record
        print(self.record)
        self.ins()

    def ins(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table()

    def table(self):

        v = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(3)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        table.setRowCount(0)

        for row_num, row_data in enumerate(self.record):
            table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                table.setItem(row_num, col_num, QTableWidgetItem(data))

        v.addWidget(table)

        self.setLayout(v)
