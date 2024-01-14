from time import time
from abstracts import AbstractStationary
from config import LEVEL_POSITION_OBJECT, SPRITE_SIZE


class Stationary(AbstractStationary):
    """ . """
    __slots__ = ("__screen", "__w", "__h", "__obj", "__begin_time", "__count", "animation",)

    def __init__(self, screen, w: int, h: int, sprites: dict) -> None:
        self.__screen = screen
        self.__w = w
        self.__h = h
        self.__obj = sprites
        self.__begin_time = time()  # Таймер;
        self.__count = 0 # Счётчик для смены изображений;
        self.animation = "bush"  # Текущая анимация;

    def timer(self) -> None:
        """ Таймер для отслеживания состояния объекта """
        end = time() - self.__begin_time
        # print(end)
        if 1.7 <= end <= 15.0:
            self.__count = 0
        elif end > 15.0:
            self.__count = 0
            self.__begin_time = time()

    def draw(self) -> None:
        """ Отрисовка неподвижного объекта """
        # Смена изображения (позволяет анимировать объект);
        if self.__count >= len(self.__obj[self.animation]):
            self.__count = 0
        _, h = self.size
        # Отрисовка различных анимаций bush;
        self.__screen.blit(
            self.__obj[self.animation][self.__count],
            (self.__w, self.__h - h - LEVEL_POSITION_OBJECT)
        )
        self.__count += 1

    @property
    def size(self) -> tuple[int, int]:
        """ Получаем размер изображения неподвижного объекта """
        return self.__obj[SPRITE_SIZE][self.animation]
