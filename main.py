import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import music_player
import sqlite3
import io
import os
from PyQt6 import uic
import threading


template_main = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1024</width>
    <height>512</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>470</y>
     <width>141</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Запустить лучший трек</string>
   </property>
   <property name="autoExclusive">
    <bool>false</bool>
   </property>
   <property name="flat">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>870</x>
     <y>480</y>
     <width>151</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Выход</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Main(QMainWindow, QDialog):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        f = io.StringIO(template_main)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.song)

    def song(self):
        self.h = threading.Thread(target=music_player, args=(self,), name='thr-1')
        self.h.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())








