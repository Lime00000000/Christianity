import sys
import io
import pyglet
import webbrowser
import sqlite3
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
    <width>683</width>
    <height>222</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>530</x>
     <y>190</y>
     <width>151</width>
     <height>31</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <widget class="QPushButton" name="pushButton_2">
      <property name="text">
       <string>Выход</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>0</y>
     <width>461</width>
     <height>51</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QComboBox" name="comboBox">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_9">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Добавить
Задачу</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_10">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Удалить
Задачу</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>60</y>
     <width>681</width>
     <height>131</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_2">
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
     <widget class="QPushButton" name="pushButton_3">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Имба Калькулятор</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget_3">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>190</y>
     <width>201</width>
     <height>31</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_3">
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
        self.reg = args[0]
        self.ac = (args[1], args[2])
        self.initUI(args)

    def initUI(self, args):
        f = io.StringIO(template_main)
        uic.loadUi(f, self)
        db = sqlite3.connect('user.db')
        cur = db.cursor()
        self.tasks = list(cur.execute(f'''SELECT task FROM user WHERE '{self.ac[0]}' = name AND '{self.ac[1]}' = password''').fetchall())
        if self.tasks:
            self.tasks = self.tasks[0]
        if self.tasks != ['None']:
            t = []
            for el in self.tasks:
                for el1 in el.split():
                    if el1 != 'None':
                        t.append(el1)
            self.tasks = t
            for el in self.tasks:
                self.comboBox.addItem(el)
        self.pushButton.clicked.connect(self.song)
        self.pushButton_2.clicked.connect(self.EXIT)
        self.pushButton_3.clicked.connect(self.Calc)
        self.pushButton_5.clicked.connect(self.tg)
        self.pushButton_4.clicked.connect(self.eat)
        self.pushButton_8.clicked.connect(self.set_dark_theme)
        self.pushButton_7.clicked.connect(self.set_light_theme)
        self.pushButton_9.clicked.connect(self.add)
        self.pushButton_10.clicked.connect(self.remove_item)

        db.commit()
        db.close()

    def add(self):
        if self.lineEdit.text() != '':
            item_to_check = self.lineEdit.text()
            index = self.comboBox.findText(item_to_check)
            if index == -1:
                self.comboBox.addItem(self.lineEdit.text())
                self.tasks.append(self.lineEdit.text())
                self.lineEdit.setText('')

    def remove_item(self):
        current_index = self.comboBox.currentIndex()
        if current_index != -1:
            self.tasks.remove(self.comboBox.itemText(current_index))
            self.comboBox.removeItem(current_index)


    def song(self):
        self.player = AudioPlayer(self)
        self.player.show()

    def EXIT(self):
        try:
            self.player.player.pause()
            self.player.close()

            self.Calculator.close()
            self.order.close()
        except Exception:
            pass

        db = sqlite3.connect('user.db')
        cur = db.cursor()

        cur.execute(f'''Update user set task = '{' '.join(self.tasks)}' where '{self.ac[0]}' = name''')
        db.commit()
        db.close()
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








