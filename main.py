import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import music_player
import register
import sqlite3
import io
import os


template_reg = ''''''


class Main(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bd = sqlite3.connect('user.db')
        cur = bd.cursor()
        query = """ INSERT INTO user (password, name) VALUES('1', 'what') """
        cur.execute(query)
        bd.commit()
        bd.close()

        print(os.system("python register.py"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec())