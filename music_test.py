import pyglet


def music_player():
    source = pyglet.media.load(filename='cool_music.mp3')
    player = pyglet.media.Player()
    player.loop = True
    player.queue(source)

    print('Press any key to play or pause!')
    while True:
        _ = input()
        if player.playing:
            player.pause()
            player.seek(0)  # (optional) rewind to the start of the source
        else:
            player.play()