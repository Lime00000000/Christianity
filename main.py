import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMainWindow, QDialog
from music_test import AudioPlayer
import io
from PyQt6 import uic
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
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>181</width>
     <height>531</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QPushButton" name="pushButton_3">
      <property name="text">
       <string>PushButton</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_4">
      <property name="text">
       <string>PushButton</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
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
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_6">
      <property name="text">
       <string>PushButton</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_5">
      <property name="text">
       <string>PushButton</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>874</x>
     <y>482</y>
     <width>150</width>
     <height>30</height>
    </rect>
   </property>
   <property name="text">
    <string>Выход</string>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>890</x>
     <y>0</y>
     <width>131</width>
     <height>80</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <widget class="QPushButton" name="pushButton_7">
      <property name="text">
       <string>Светлая тема</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_8">
      <property name="text">
       <string>Темная тема</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>



'''


class Main(QDialog):
    def __init__(self, *args):
        super().__init__()
        if not args:
            args = '123'
        self.initUI(args)
        self.reg = args[0]

    def initUI(self, args):
        f = io.StringIO(template_main)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.song)
        self.pushButton_2.clicked.connect(self.EXIT)
        self.pushButton_8.clicked.connect(self.set_dark_theme)
        self.pushButton_7.clicked.connect(self.set_light_theme)

    def song(self):
        self.player = AudioPlayer(self)
        self.player.show()

    def EXIT(self):
        try:
            self.player.player.pause()
            self.player.close()
        except Exception:
            pass
        self.reg.show()
        self.close()

    def set_light_theme(self):
        self.setStyleSheet("background-color: white; color: black;")
        self.pushButton.setStyleSheet(
            'QPushButton {background-color: white; border: 2px solid black; border-radius: 5px;}')
        for i in range(2, 9):
            g = f"self.pushButton_{i}.setStyleSheet(" + "'QPushButton {background-color: white; border: 2px solid black; border-radius: 5px;}'" + ")"
            exec(g)


    def set_dark_theme(self):
        self.setStyleSheet("background-color: rgb(30, 30, 30));")
        self.pushButton.setStyleSheet(
            'QPushButton {background-color: rgb(60, 60, 60);}')
        for i in range(2, 9):
            g = f"self.pushButton_{i}.setStyleSheet(" + "'QPushButton {background-color: rgb(60, 60, 60);}'" + ")"
            exec(g)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    pyglet.app.run()
    sys.exit(app.exec())








