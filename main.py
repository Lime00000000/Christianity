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
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>160</width>
     <height>511</height>
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
 </widget>
 <resources/>
 <connections/>
</ui>

'''


class Main(QMainWindow, QDialog):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.reg = args[0]

    def initUI(self, args):
        f = io.StringIO(template_main)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.song)
        self.pushButton_2.clicked.connect(self.EXIT)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    pyglet.app.run()
    sys.exit(app.exec())








