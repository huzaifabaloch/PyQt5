from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtGui
import sys


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Web on mind'
        self.left = 300
        self.top = 150
        self.width = 500
        self.height = 500
        self.icon = 'venv\cowweb.ico'

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.creating_tables()

        self.show()

    def creating_tables(self):

        table_widget = QTableWidget()
        vbox = QVBoxLayout()

        table_widget.setRowCount(5)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem('Name'))
        table_widget.setItem(0, 1, QTableWidgetItem('Email'))
        table_widget.setItem(0, 2, QTableWidgetItem('Phone'))

        table_widget.setItem(1, 0, QTableWidgetItem('Tuna'))
        table_widget.setItem(1, 1, QTableWidgetItem('tuna@mail.com'))
        table_widget.setItem(1, 2, QTableWidgetItem('023-230-2'))

        vbox.addWidget(table_widget)

        self.setLayout(vbox)



App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
