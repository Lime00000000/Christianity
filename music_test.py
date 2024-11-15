from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QFileDialog, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt6.QtMultimedia import QMediaPlayer, QMediaFormat
from PyQt6.QtCore import Qt, QUrl
import sys


class MusicPlayer(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle("Good")
        self.setGeometry(100, 100, 300, 400)
        self.media_player = QMediaPlayer()
        self.setup_ui(args)

    def setup_ui(self, *args):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        button_layout = QVBoxLayout()

        open_btn = QPushButton("Open")
        open_btn.clicked.connect(self.open_file)
        button_layout.addWidget(open_btn)

        play_btn = QPushButton("Play")
        play_btn.clicked.connect(self.media_player.play)
        button_layout.addWidget(play_btn)

        pause_btn = QPushButton("Pause")
        pause_btn.clicked.connect(self.media_player.pause)
        button_layout.addWidget(pause_btn)

        stop_btn = QPushButton("Stop")
        stop_btn.clicked.connect(self.media_player.stop)
        button_layout.addWidget(stop_btn)

        main_layout.addLayout(button_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def open_file(self):
        self.media_player.setSource(QUrl.fromLocalFile("cool_music.mp3"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicPlayer()
    ex.show()
    sys.exit(app.exec())