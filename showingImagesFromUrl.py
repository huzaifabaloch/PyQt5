from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import urllib.request


class Root(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'product box'
        self.left = 500
        self.top = 150
        self.width = 500
        self.height = 500
        self.icon = 'venv\cowweb.ico'

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.product_page()
        self.show()

    def product_page(self):

        url = 'https://images-na.ssl-images-amazon.com/images/I/81d6JU6g1pL._AC_SX215_.jpg'
        data = urllib.request.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)

        pixmap = QtGui.QPixmap(image)
        pixmap = pixmap.scaledToWidth(200, 200)


        label = QLabel(self)
        label.setPixmap(QtGui.QPixmap(pixmap))
        label.setGeometry(20, 30, 400, 300)


App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
