from sys import exit
from pygame import (time, image, transform, init, display, quit, event, key, RESIZABLE, QUIT,
                    MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT)
from config import FPS, isGAME, Palette as P
from timer import GameTimer


class Engine:
    """ Игровой 2D движок """
    __slots__ = ("__form", "__timer", "__w", "__h", "__screen", "__bg",)

    def __init__(self) -> None:
        """ Инициализация pygame """
        init()
        self.__form = display
        # self.__timer = Timer()

    def window(self, w: int, h: int, title: str="Untitled", icon: str=None, bg: str = None) -> display:
        """ Создаём рабочее окно (также название окна и иконку) """
        self.__w = w
        self.__h = h
        self.__screen = self.__form.set_mode((self.__w, self.__h), RESIZABLE)
        self.__form.set_caption(title)
        if icon is not None:
            self.__form.set_icon(image.load(icon))
        if bg is not None:
            self.__bg = transform.scale(image.load(bg), (self.__w, self.__h))
        return self.__screen

    def get_size(self) -> tuple[int, int]:
        """ Получаем размеры рабочего окна """
        return self.__w, self.__h

    def loop(self, *args, **kwargs) -> None:
        """ Игровой бесконечный цикл """
        # self.__timer.add_action(0.2, kwargs["fox"].set_animation, "stop")
        # self.__timer.add_action(4.7, kwargs["fox"].set_animation, "stop_to_sleep")
        # self.__timer.add_action(5.0, kwargs["fox"].set_animation, "sleep")
        while isGAME:
            time.delay(FPS)
            # self.__screen.fill(P.BLACK)
            self.__screen.blit(self.__bg, (0, 0))
            # Таймер для анимаций
            # self.__timer.check()
            kwargs["fox"].timer()
            kwargs["bush"].timer()

            for action in event.get():
                if action.type == QUIT:
                    quit()
                elif action.type == KEYDOWN:  # | K_LEFT | K_RIGHT | K_UP | K_DOWN | K_SPACE |
                    if action.key == K_UP:
                        kwargs["fox"].move_up()
                    elif action.key == K_DOWN:
                        kwargs["fox"].move_down()

            # Зажатие клавиш;
            KEY_PRESSED = key.get_pressed()
            if KEY_PRESSED[K_LEFT]:
                kwargs["fox"].move_left()
            elif KEY_PRESSED[K_RIGHT]:
                kwargs["fox"].move_right()

            kwargs["fox"].draw()
            kwargs["bush"].draw()
            # Обновляем рабочий экран;
            self.__form.update()

    def __del__(self) -> None:
        """ Чтобы закрыть окно pygame """
        quit()


# def close_all() -> None:
#     """ Закрываем окно pygame и выходим из программы """
#     quit()
#     exit()
