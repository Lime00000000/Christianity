import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>591</width>
    <height>472</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPlainTextEdit" name="text_edit">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>100</y>
     <width>191</width>
     <height>231</height>
    </rect>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>100</y>
     <width>160</width>
     <height>231</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLineEdit" name="filename_edit"/>
    </item>
    <item>
     <widget class="QPushButton" name="new_button">
      <property name="text">
       <string>Создать</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="save_button">
      <property name="text">
       <string>Сохранить</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="open_button">
      <property name="text">
       <string>Открыть</string>
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


class Notebook(QDialog):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(500, 400)

        self.new_button.clicked.connect(self.NEW)
        self.save_button.clicked.connect(self.save)
        self.open_button.clicked.connect(self.open)

    def NEW(self):
        self.text_edit.clear()
        self.filename_edit.clear()

    def open(self):
        try:
            a = open(self.filename_edit.text(), 'r').readlines()
            for el in a:
                self.text_edit.insertPlainText(el)
        except Exception:
            pass

    def save(self):
        try:
            with open(self.filename_edit.text(), 'w') as g:
                for el in self.text_edit.toPlainText():
                    g.write(el)
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())
