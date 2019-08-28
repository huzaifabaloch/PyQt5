from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QCompleter
from PyQt5.QtGui import QIcon, QFont
import sys
import mysql.connector as sql


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'search bar'
        self.left = 300
        self.top = 100
        self.width = 400
        self.height = 400
        self.icon = 'venv\cowweb.ico'
        self.games = []
        self.product_names()

        self.init_window()

    def product_names(self):

        conn = sql.connect(
            host='localhost',
            user='root',
            passwd='abc123',
            database='web_on_mind'
        )
        cur = conn.cursor()

        cur.execute('SELECT name_of_game FROM ps4_tbl')
        result = cur.fetchall()

        for row in result:
            for e in row:
                self.games.append(e.lower())

        print(self.games)

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ui_components()

        self.show()


    def ui_components(self):
        vbox = QVBoxLayout()

        compeleter = QCompleter(self.games)

        self.search = QLineEdit(self)
        self.search.setCompleter(compeleter)
        self.search.setPlaceholderText('Search')
        self.search.setFont(QFont('Calibri', 20))
        self.search.setStyleSheet("color:grey")
        vbox.addWidget(self.search)

        self.setLayout(vbox)



App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
