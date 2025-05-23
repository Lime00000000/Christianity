from PyQt6.QtWidgets import QInputDialog, QDialog, QApplication
import sys
import io
from PyQt6 import uic
import sqlite3
from main import Main


template_reg = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1025</width>
    <height>529</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>160</x>
     <y>350</y>
     <width>701</width>
     <height>51</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <property name="spacing">
     <number>50</number>
    </property>
    <item>
     <widget class="QPushButton" name="inbtn">
      <property name="text">
       <string>Я хочу стать смешариком</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="new_inbtn">
      <property name="text">
       <string>Я уже смешарик</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>500</y>
     <width>271</width>
     <height>21</height>
    </rect>
   </property>
   <property name="lineWidth">
    <number>16</number>
   </property>
   <property name="midLineWidth">
    <number>14</number>
   </property>
   <property name="text">
    <string>Чтобы стать boss of the gym, необходимо воркать...</string>
   </property>
  </widget>
 </widget>
 <resources>
  <include location="../../Downloads/21113999-85ae-5494-a4ce-56786b2eb509.qrc"/>
 </resources>
 <connections/>
</ui>
'''


class Pseudonym(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_reg)
        uic.loadUi(f, self)
        self.inbtn.clicked.connect(self.reg)
        self.new_inbtn.clicked.connect(self.reg_old)

    def reg(self):
        bd = sqlite3.connect('user.db')
        cur = bd.cursor()
        g = 'Придумайте логин'
        flag = True
        while flag:
            login, ok = QInputDialog.getText(self, ' ', g)
            query1 = f""" SELECT name FROM user WHERE name = '{login}' """
            if ok and login and not cur.execute(query1).fetchall():
                while flag:
                    password, ok = QInputDialog.getText(self, ' ', 'Придумайте пароль')
                    if ok and password:
                        query = f""" INSERT INTO user (password, name, task) VALUES('{login}', '{password}', '{None}') """
                        cur.execute(query)
                        bd.commit()
                        bd.close()
                        self.h = Main(self, login, password)
                        self.hide()
                        self.h.show()
                        flag = False
                        break
                    if not ok:
                        break
                break
            if cur.execute(query1).fetchall():
                g = 'Такое уже есть'
            if not ok:
                break

    def reg_old(self):
        bd = sqlite3.connect('user.db')
        cur = bd.cursor()
        flag = True
        while flag:
            login, ok = QInputDialog.getText(self, ' ', 'Введите логин')
            query1 = f""" SELECT name FROM user WHERE name = '{login}' """
            if ok and login and cur.execute(query1).fetchall():
                while flag:
                    password, ok = QInputDialog.getText(self, ' ', 'Введите пароль')
                    query2 = f""" SELECT password FROM user WHERE name = '{login}' """
                    if ok and password == cur.execute(query2).fetchall()[0][0]:
                        self.h = Main(self, login, password)
                        self.hide()
                        self.h.show()
                        flag = False
                        break
                    if not ok:
                        break
            if not ok:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())