import io
import sys
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6 import uic
from math import sqrt


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>371</width>
    <height>565</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Красивый калькулятор</string>
  </property>
  <widget class="QWidget" name="layoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>345</width>
     <height>481</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLCDNumber" name="table"/>
    </item>
    <item>
     <layout class="QGridLayout" name="gridLayout">
      <item row="2" column="1">
       <widget class="QPushButton" name="btn8">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>8</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="1">
       <widget class="QPushButton" name="btn2">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>2</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="3">
       <widget class="QPushButton" name="btn_plus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>+</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="2">
       <widget class="QPushButton" name="btn_eq">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>=</string>
        </property>
       </widget>
      </item>
      <item row="3" column="0">
       <widget class="QPushButton" name="btn0">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>0</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="3">
       <widget class="QPushButton" name="btn_div">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>/</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="0">
       <widget class="QPushButton" name="btn1">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>1</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="2">
       <widget class="QPushButton" name="btn9">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>9</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="1">
       <widget class="QPushButton" name="btn_dot">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>.</string>
        </property>
       </widget>
      </item>
      <item row="0" column="2">
       <widget class="QPushButton" name="btn3">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>3</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="0">
       <widget class="QPushButton" name="btn4">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>4</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="1">
       <widget class="QPushButton" name="btn5">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>5</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="0">
       <widget class="QPushButton" name="btn7">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>7</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="2">
       <widget class="QPushButton" name="btn6">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>6</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="3">
       <widget class="QPushButton" name="btn_minus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>-</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="3">
       <widget class="QPushButton" name="btn_mult">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>*</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="0">
       <widget class="QPushButton" name="btn_pow">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>^</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="1">
       <widget class="QPushButton" name="btn_sqrt">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>√</string>
        </property>
       </widget>
      </item>
      <item row="4" column="2">
       <widget class="QPushButton" name="btn_fact">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>!</string>
        </property>
       </widget>
      </item>
      <item row="4" column="3">
       <widget class="QPushButton" name="btn_clear">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">background-color: rgb(254, 166, 43);</string>
        </property>
        <property name="text">
         <string>С</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup_binary"/>
  <buttongroup name="buttonGroup_digits"/>
 </buttongroups>
</ui>
'''


def fac(a):
    if a == 0:
        return 1
    return a * fac(a - 1)


class Calculator(QDialog):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(380, 512)

        self.k = 0
        self.k1 = ''

        self.btn_clear.clicked.connect(self.clear_)

        self.btn_plus.clicked.connect(self.hitpl)

        self.btn_minus.clicked.connect(self.hitmn)

        self.btn0.clicked.connect(self.hitnum)
        self.btn1.clicked.connect(self.hitnum)
        self.btn2.clicked.connect(self.hitnum)
        self.btn3.clicked.connect(self.hitnum)
        self.btn4.clicked.connect(self.hitnum)
        self.btn5.clicked.connect(self.hitnum)
        self.btn6.clicked.connect(self.hitnum)
        self.btn7.clicked.connect(self.hitnum)
        self.btn8.clicked.connect(self.hitnum)
        self.btn9.clicked.connect(self.hitnum)

        self.btn_eq.clicked.connect(self.btn_eq1)

        self.btn_mult.clicked.connect(self.btn_mult1)

        self.btn_div.clicked.connect(self.btn_div1)

        self.btn_dot.clicked.connect(self.btn_dot1)

        self.btn_pow.clicked.connect(self.btn_pow1)

        self.btn_sqrt.clicked.connect(self.btn_sqrt1)

        self.btn_fact.clicked.connect(self.btn_fact1)

        self.u = '0'

    def hitnum(self):
        if self.table.value() != 0.0 and self.u != '0':
            self.u += self.sender().objectName()[-1]
            self.table.display(self.u)
        else:
            self.u = self.sender().objectName()[-1]
            self.table.display(self.u)

    def clear_(self):
        self.table.display(0)
        self.k = 0
        self.u = '0'

    def hitpl(self):
        self.k1 = '+'
        self.k = self.table.value()
        self.table.display(0)
        self.u = '0'

    def hitmn(self):
        self.k1 = '-'
        self.k = self.table.value()
        self.table.display(0)
        self.u = '0'

    def btn_mult1(self):
        self.k1 = '*'
        self.k = self.table.value()
        self.table.display(0)
        self.u = '0'

    def btn_div1(self):
        self.k1 = '/'
        self.k = self.table.value()
        self.table.display(0)
        self.u = '0'

    def btn_eq1(self):
        try:
            self.table.display(float(eval(f'{self.k} {self.k1} {self.table.value()}')))
            self.k1 = ''
            self.k = 0
            self.u = '0'
        except Exception:
            self.k1 = ''
            self.k = 0
            self.table.display('error')
            self.u = '0'

    def btn_dot1(self):
        if not ('.' in self.u):
            self.u += '.'
            self.table.display(self.u)

    def btn_pow1(self):
        self.k1 = '**'
        self.k = self.table.value()
        self.table.display(0)
        self.u = '0'

    def btn_sqrt1(self):
        self.table.display(sqrt(self.table.value()))
        self.k1 = ''
        self.k = 0

    def btn_fact1(self):
        self.table.display(fac(self.table.value()))
        self.k1 = ''
        self.k = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())