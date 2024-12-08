import sys
from PyQt6.QtGui import QImage, QTransform, QPixmap, qRgb
from PyQt6.QtWidgets import QFileDialog, QApplication, QDialog, QLabel, QButtonGroup
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
    <width>854</width>
    <height>825</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>110</y>
     <width>101</width>
     <height>251</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="channelButtons">
    <item>
     <widget class="QPushButton" name="Red">
      <property name="text">
       <string>R</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="Green">
      <property name="text">
       <string>G</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="Blue">
      <property name="text">
       <string>B</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="All">
      <property name="text">
       <string>ALL</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>250</x>
     <y>370</y>
     <width>261</width>
     <height>31</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="rotateButtons">
    <item>
     <widget class="QPushButton" name="minus">
      <property name="text">
       <string>Против часовой стрелки</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="plus">
      <property name="text">
       <string>По часовой стрелке</string>
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


class MyPillow(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.UIinit()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(800, 600)

        self.channelButtons = QButtonGroup()
        self.rotateButtons = QButtonGroup()

        self.Green.clicked.connect(self.hit)
        self.Red.clicked.connect(self.hit)
        self.Blue.clicked.connect(self.hit)
        self.All.clicked.connect(self.hit)

        self.channelButtons.addButton(self.Green)
        self.channelButtons.addButton(self.Red)
        self.channelButtons.addButton(self.Blue)
        self.channelButtons.addButton(self.All)

        self.minus.clicked.connect(self.hitpl)
        self.plus.clicked.connect(self.hitpl)

        self.rotateButtons.addButton(self.minus)
        self.rotateButtons.addButton(self.plus)
        self.angle = 0

    def UIinit(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.real, self.curr_image = QImage(fname), QImage(fname)
        self.pixmap = QPixmap(self.curr_image.copy())
        self.image = QLabel(self)
        self.image.move(260, 110)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

    def hit(self):
        self.curr_image = self.real.copy()
        self.pixmap = QPixmap(self.curr_image.copy())
        if self.sender().text() != 'ALL':
            x, y = self.pixmap.size().width(), self.pixmap.size().height()
            for i in range(y):
                for j in range(x):
                    r, g, b, a = self.real.pixelColor(j, i).getRgb()
                    r, g, b = ((self.sender().text() == 'R') * r, (self.sender().text() == 'G') * g,
                               (self.sender().text() == 'B') * b)
                    self.curr_image.setPixel(j, i, qRgb(r, g, b))

        self.curr_image = self.curr_image.transformed(QTransform().rotate(self.angle))
        self.pixmap = QPixmap(self.curr_image.copy())
        self.image.setPixmap(self.pixmap)

    def hitpl(self):
        if self.sender().text() == 'Против часовой стрелки':
            k = -90
            self.angle -= 90
        else:
            k = 90
            self.angle += 90
        self.curr_image = self.curr_image.transformed(QTransform().rotate(k))
        self.pixmap = QPixmap(self.curr_image)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())