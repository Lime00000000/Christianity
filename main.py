import sys
import io
import pyglet
import webbrowser
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from music_test import AudioPlayer
from set_theme import set_light_theme, set_dark_theme
from calculator import Calculator
from order import Food


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
     <height>511</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <property name="spacing">
     <number>25</number>
    </property>
    <property name="bottomMargin">
     <number>0</number>
    </property>
    <item>
     <widget class="QPushButton" name="pushButton_3">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Имба Калькулятор на 200 строк</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_4">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Кушать</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Плеер с лучшим</string>
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
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>PushButton</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_5">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Если хочешь в IT и тебе
не нужна шкила</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>874</x>
     <y>471</y>
     <width>150</width>
     <height>41</height>
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
        self.pushButton_3.clicked.connect(self.Calc)
        self.pushButton_5.clicked.connect(self.tg)
        self.pushButton_4.clicked.connect(self.eat)
        self.pushButton_8.clicked.connect(self.set_dark_theme)
        self.pushButton_7.clicked.connect(self.set_light_theme)

    def song(self):
        self.player = AudioPlayer(self)
        self.player.show()

    def EXIT(self):
        try:
            self.player.player.pause()
            self.player.close()

            self.Calculator.close()
        except Exception:
            pass
        self.reg.show()
        self.close()

    def Calc(self):
        self.Calculator = Calculator(self)
        self.Calculator.show()

    def tg(self):
        webbrowser.open('t.me/tset03_bot')

    def eat(self):
        self.order = Food(self)
        self.order.show()

    def set_dark_theme(self):
        set_dark_theme(self)

    def set_light_theme(self):
        set_light_theme(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    pyglet.app.run()
    sys.exit(app.exec())








