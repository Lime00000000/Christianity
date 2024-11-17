import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit, QLineEdit


CODE = {"Чизбургер": 10,
        "Гамбургер": 20,
        "Кока-кола": 15,
        "Наггетсы": 30}

CODE1 = {"Чизбургер": 0,
         "Гамбургер": 1,
         "Кока-кола": 2,
         "Наггетсы": 3}


class Food(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, *args):
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Заказ')

        self.h = QCheckBox(self)
        self.h.setText('Чизбургер')

        self.h1 = QCheckBox(self)
        self.h1.setText('Гамбургер')
        self.h1.move(0, 20)

        self.h2 = QCheckBox(self)
        self.h2.setText('Кока-кола')
        self.h2.move(0, 40)

        self.h3 = QCheckBox(self)
        self.h3.setText('Наггетсы')
        self.h3.move(0, 60)

        self.checkboxes = [self.h, self.h1, self.h2, self.h3]

        self.orderButton = QPushButton(self)
        self.orderButton.setGeometry(0, 0, 100, 20)
        self.orderButton.setText('Заказать')
        self.orderButton.move(0, 90)

        self.orderButton.clicked.connect(self.hit)

        self.order = QPlainTextEdit(self)
        self.order.move(0, 120)

        self.inputs = []
        h = 10
        for i in range(7):
            if i == 0 or i % 2 == 0:
                chesse = QLineEdit(self)
                chesse.setGeometry(0, 0, 40, 20)
                chesse.move(100, h * i)
                chesse.setEnabled(False)
                self.inputs.append(chesse)

        self.h.clicked.connect(self.hitmenu)
        self.h1.clicked.connect(self.hitmenu)
        self.h2.clicked.connect(self.hitmenu)
        self.h3.clicked.connect(self.hitmenu)

    def hit(self):
        self.order.clear()
        self.order.insertPlainText('Ваш заказ' + '\n' + '\n')
        z = 0
        for el in self.checkboxes:
            if el.isChecked():
                b = '-----'
                z += CODE[el.text()] * int(self.inputs[CODE1[el.text()]].text())
                self.order.insertPlainText(el.text() + b + self.inputs[CODE1[el.text()]].text() + b
                                           + str(CODE[el.text()] * int(self.inputs[CODE1[el.text()]].text())) + '\n')
        self.order.insertPlainText('\n')
        self.order.insertPlainText(f'Итого: {z}')

    def hitmenu(self):
        p = self.sender().text()
        if self.sender().isChecked():
            self.inputs[CODE1[p]].setEnabled(True)
        else:
            self.inputs[CODE1[p]].setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Food()
    ex.show()
    sys.exit(app.exec())