def set_light_theme(self):
    self.setStyleSheet("background-color: white; color: black;")
    self.pushButton.setStyleSheet(
        'QPushButton {background-color: white; border: 2px solid black; border-radius: 5px;}')
    for i in range(2, 11):
        g = f"self.pushButton_{i}.setStyleSheet(" + "'QPushButton {background-color: white; border: 2px solid black; border-radius: 5px;}'" + ")"
        exec(g)


def set_dark_theme(self):
    self.setStyleSheet("background-color: rgb(30, 30, 30));")
    self.pushButton.setStyleSheet(
        'QPushButton {background-color: rgb(60, 60, 60);}')
    for i in range(2, 11):
        g = f"self.pushButton_{i}.setStyleSheet(" + "'QPushButton {background-color: rgb(60, 60, 60);}'" + ")"
        exec(g)