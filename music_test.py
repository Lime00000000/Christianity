import pyglet
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys


class AudioPlayer(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.initUI(args)

        self.player = pyglet.media.Player()
        self.source = pyglet.media.load('cool_music.mp3')
        self.player.queue(self.source)
        self.player.loop = True

        self.setWindowTitle('Audio Player')
        self.setGeometry(100, 100, 300, 200)

    def initUI(self, *args):
        self.button = QPushButton('Запустить лучший трек', self)
        self.button.clicked.connect(self.toggle_music)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def toggle_music(self):
        if self.player.playing:
            self.player.pause()
            self.button.setText('Запустить лучший трек')
        else:
            self.player.play()
            self.button.setText('Остановить')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    pyglet.app.run()
    sys.exit(app.exec())
