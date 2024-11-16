import pyglet


def music_player(window):
    source = pyglet.media.load(filename='cool_music.mp3')
    player = pyglet.media.Player()
    player.loop = True
    player.queue(source)
    if window.pushButton.text() == 'Запустить лучший трек':
        player.play()
    else:
        window.pushButton.setText('Остановить')
        player.pause()
        player.seek(0)