from pygame import (time, image, transform, init, display, quit, event, key,
                    MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, KEYDOWN,
                    RESIZABLE, QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, Surface)
from abstracts import AbstractWindow
from config import DIR_IMG


class Window(AbstractWindow):
    """ Главное окно приложения """
    __slots__ = ("__form", "__w", "__h", "__title", "__icon", "__bg", "__screen",)

    def __init__(self, w: int, h: int, icon: str, bg: str, title: str = "Untitled") -> None:
        init()
        self.__form = display
        self.__w = w  # Ширина окна
        self.__h = h  # Высота окна
        self.__create(icon, bg, title)

    def __create(self, icon: str, bg: str, title: str = "Untitled") -> None:
        """ Создаём рабочее окно (также название окна и иконку) """
        self.__screen = self.__form.set_mode(self.size, RESIZABLE)
        # Устанавливаем название окна приложения
        self.__form.set_caption(title)
        # Устанавливаем иконку окна приложения
        self.__form.set_icon(image.load(f"{DIR_IMG}{icon}"))
        # Устанавливаем фон окна приложения
        self.__bg = transform.scale(image.load(f"{DIR_IMG}{bg}"), self.size)

    def screen_blit(self) -> None:
        """ Обновить фон окна приложения """
        self.__screen.blit(self.__bg, (0, 0))

    def form_update(self) -> None:
        """ Обновить экран окна приложения """
        self.__form.update()

    @property
    def screen(self) -> display:
        """ Получить объект для работы с окном приложения """
        return self.__screen

    @property
    def size(self) -> tuple[int, int]:
        """ Получить размеры окна приложения """
        return self.__w, self.__h

    def __del__(self) -> None:
        """ Закрыть окно приложения """
        quit()
