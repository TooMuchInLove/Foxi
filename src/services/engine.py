from pygame import (time, quit, event, key, QUIT, MOUSEMOTION, MOUSEBUTTONUP,
                    MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT)
from abstracts import AbstractWindow
from config import FPS, is_game


class Engine2D:
    """ Игровой 2D движок """
    __slots__ = ("__window", "__hero", "__bush",)

    def __init__(self, window: AbstractWindow) -> None:
        self.__window = window

    def loop(self, hero, bush) -> None:  # FIXME: переделать
        """ Игровой бесконечный цикл """
        while is_game:
            # Частота обновления окна приложения
            time.delay(FPS)
            # Отрисовка фона окна приложения
            self.__window.screen_blit()
            # Таймер для анимаций
            hero.timer()
            bush.timer()
            # Цикл для определения нажатия клавиш
            for action in event.get():
                if action.type == QUIT:
                    quit()
                elif action.type == KEYDOWN:  # | K_LEFT | K_RIGHT | K_UP | K_DOWN | K_SPACE |
                    if action.key == K_UP:
                        hero.move_up()
                    elif action.key == K_DOWN:
                        hero.move_down()
            # Зажатие клавиш;
            KEY_PRESSED = key.get_pressed()
            if KEY_PRESSED[K_LEFT]:
                hero.move_left()
            elif KEY_PRESSED[K_RIGHT]:
                hero.move_right()
            # Отрисовка объектов
            hero.draw()
            bush.draw()
            # Обновление окна приложения
            self.__window.form_update()
