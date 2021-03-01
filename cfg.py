import os


BGMPATH = os.path.join(os.getcwd(), 'resources/music/bgm.mp3')
FONTPATH = os.path.join(os.getcwd(), 'resources/font/Gabriola.ttf')
SCREENSIZE = (800, 500)
# кадры(fps)
FPS = 5
# константы
BLOCK_SIZE = 20
BLACK = (0, 0, 0)
GAME_MATRIX_SIZE = (int(SCREENSIZE[0]/BLOCK_SIZE), int(SCREENSIZE[1]/BLOCK_SIZE))
