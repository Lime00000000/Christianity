import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import music_player
from register import Pseudonym
import sqlite3
import io
import os


class Main(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        self.hide()
        self.initUI()


    def initUI(self):
        self.h = Pseudonym(self)
        self.h.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())








