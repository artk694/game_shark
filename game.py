import cfg
import sys
import pygame
from modules import *


def main(cfg):
    # основа
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('proekt yandex lyceum')
    clock = pygame.time.Clock()
    # фоновая музыка
    pygame.mixer.music.load(cfg.BGMPATH)
    pygame.mixer.music.play(-1)
    # Основной цикл игры
    snake = Snake(cfg)
    apple = Apple(cfg, snake.coords)
    score = 0
    while True:
        screen.fill(cfg.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    snake.setDirection({pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left',
                                        pygame.K_RIGHT: 'right'}[event.key])
        # обновление змеи и еды для неё
        if snake.update(apple):
            apple = Apple(cfg, snake.coords)
            score += 1
        # когда врезается в стену заканчивает игру или когда ест сам себя
        if snake.isgameover:
            break
        # элементы в игре
        drawGameGrid(cfg, screen)
        snake.draw(screen)
        apple.draw(screen)
        showScore(cfg, score, screen)
        # Обновляет экран при начале
        pygame.display.update()
        clock.tick(cfg.FPS)
    return endInterface(screen, cfg)
# экран при конце игры

'''начало игры'''
if __name__ == '__main__':
    while True:
        if not main(cfg):
            break


'''конец игры'''
