from pygame import (time, quit, event, key, QUIT, MOUSEMOTION, MOUSEBUTTONUP,
                    MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT)
from abstracts import AbstractWindow
from services import Hero, Stationary, loading_sprites
from config import FPS, SPRITES, is_game


class Engine2D:
    """ Игровой 2D движок """
    __slots__ = ("__window", "__hero", "__bush", "__w", "__h",)

    def __init__(self, window: AbstractWindow) -> None:
        self.__window = window
        w, h = self.__window.size
        self.__hero = Hero(self.__window.screen, w, h, loading_sprites(SPRITES["fox"]))
        self.__bush = Stationary(self.__window.screen, w*0, h, loading_sprites(SPRITES["bush"]))

    def loop(self, *args, **kwargs) -> None:
        """ Игровой бесконечный цикл """
        while is_game:
            time.delay(FPS)
            self.__window.screen_blit()
            # Таймер для анимаций
            self.__hero.timer()
            self.__bush.timer()

            for action in event.get():
                if action.type == QUIT:
                    quit()
                elif action.type == KEYDOWN:  # | K_LEFT | K_RIGHT | K_UP | K_DOWN | K_SPACE |
                    if action.key == K_UP:
                        self.__hero.move_up()
                    elif action.key == K_DOWN:
                        self.__hero.move_down()

            # Зажатие клавиш;
            KEY_PRESSED = key.get_pressed()
            if KEY_PRESSED[K_LEFT]:
                self.__hero.move_left()
            elif KEY_PRESSED[K_RIGHT]:
                self.__hero.move_right()

            self.__hero.draw()
            self.__bush.draw()

            self.__window.form_update()
