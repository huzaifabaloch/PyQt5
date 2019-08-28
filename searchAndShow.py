from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QCompleter, QPushButton
from PyQt5.QtGui import QIcon
import sys
import mysql.connector as sql


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'search and show'
        self.left = 400
        self.top = 200
        self.width = 300
        self.height = 300
        self.icon = 'venv\cowweb.ico'
        self.games = []
        self.product_names()

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        completer = QCompleter(self.games)
        self.search = QLineEdit(self)
        self.search.setPlaceholderText('Search')
        self.search.setCompleter(completer)
        vbox.addWidget(self.search)

        btn = QPushButton('Search Game', self)
        btn.clicked.connect(self.search_game)
        vbox.addWidget(btn)

        self.setLayout(vbox)

        self.show()

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

        conn.close()

    def search_game(self):

        game_name = self.search.text()

        conn = sql.connect(
            host='localhost',
            user='root',
            passwd='abc123',
            database='web_on_mind'
        )
        cur = conn.cursor()

        cur.execute('SELECT name_of_game, price FROM ps4_tbl WHERE name_of_game = %s', (game_name,))

        result = cur.fetchone()
        if result is not None:
            print(result)
        else:
            print('No such product at the moment')


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
