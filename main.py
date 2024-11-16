import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import AudioPlayer
import sqlite3
import io
import os
from PyQt6 import uic
import threading
import pyglet


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
    <string>Плеер</string>
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
        self.pushButton_2.clicked.connect(self.pr)

    def song(self):
        self.h = AudioPlayer(self)
        self.h.show()

    def pr(self):
        print('wefwefwef')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    pyglet.app.run()
    sys.exit(app.exec())








