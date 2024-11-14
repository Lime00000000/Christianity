from PyQt6.QtWidgets import QInputDialog, QMainWindow, QDialog, QApplication
import sys
import io
from PyQt6 import uic


template = '''<?xml version="1.0" encoding="UTF-8"?>
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
       <string>Я уже смешарик</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="new_inbtn">
      <property name="text">
       <string>Я хочу стать смешариком</string>
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


def reg():
    pass


class Pseudonym(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.inbtn.clicked.connect(self.reg)

    def reg(self):
        check = False
        while True:
            login, ok = QInputDialog.getText(self, ' ', 'Введите логин')
            if ok and login:
                while True:
                    password, ok = QInputDialog.getText(self, ' ', 'Введите пароль')
                    if ok and password:
                        check = True
                        break
                    if ok is False:
                        break
                break
            if ok is False:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())








