from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys


class Root(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Wallpaper'
        self.left = 400
        self.top = 200
        self.width = 400
        self.height = 400
        self.icon = 'cowweb.ico'

        self.start_window()


    def start_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)

        self.show()

    def create_layout(self):
        self.groupbox = QGroupBox()
        hbox_layout = QHBoxLayout()

        lbl1 = QLabel('I am Label 1')
        hbox_layout.addWidget(lbl1)

        lbl2 = QLabel('I am Label 2')
        hbox_layout.addWidget(lbl2)

        lbl_image = QLabel()
        image = QPixmap('me.png')
        lbl_image.setPixmap(image)
        hbox_layout.addWidget(lbl_image)

        self.groupbox.setLayout(hbox_layout)


App =  QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
