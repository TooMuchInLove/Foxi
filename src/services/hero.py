from time import time
from pygame import transform
# from services import GameTimer
from mixins import MixinAnimationSleep, MixinAnimationStop, MixinAnimationMove
from abstracts import AbstractCharacter
from config import LEVEL_POSITION_OBJECT, INCREASE, SPRITE_SIZE, Action as A


class Hero(AbstractCharacter, MixinAnimationSleep, MixinAnimationStop, MixinAnimationMove):
    """ Класс главного героя """
    __slots__ = ("__screen", "__w", "__h", "__hero", "__begin_time", "__count",
                 "__is_flip", "__speed", "animation", "x", "y",)

    def __init__(self, screen, w: int, h: int, sprites: dict) -> None:
        self.__screen = screen
        self.__w = w
        self.__h = h
        self.__hero = sprites
        self.__begin_time = time()  # Таймер;
        # self.__timer = GameTimer()  # Таймер;
        self.__count = 0  # Счётчик для смены изображений;
        self.__is_flip = False  # Смена направления движения;
        self.__speed = 20  # Скорость передвижения персонажа;
        self.animation = A.STOP  # Текущая анимация;
        self.__set_position_hero()  # Начальные координаты персонажа;

    def start(self, current_time: float = None) -> None:
        """ Установить таймер """
        self.__begin_time = time() if current_time is None else current_time

    def timer(self) -> None:
        """ Таймер для отслеживания состояния персонажа """
        # self.__timer.tick(self.set_animation, self.animation)
        end = time() - self.__begin_time
        # print(end)
        if end >= 5.0:
            self.set_animation(A.SLEEP)
        elif end >= 4.7:
            self.set_animation(A.STOP_TO_SLEEP)
        elif end >= 0.2:
            self.set_animation(A.STOP)

    def draw(self) -> None:
        """ Отрисовка персонажа """
        # Выбираем изображение-анимации персонажа;
        sprite = self.__hero[self.animation]
        # Смена изображения (позволяет анимировать персонажа);
        if self.__count >= len(sprite):
            self.__count = 0
        # Отрисовка персонажа покадрово;
        self.__screen.blit(transform.flip(
            sprite[self.__count],
            self.__is_flip, False), self.__get_position_hero()
        )
        self.__count += 1

    @property
    def size(self) -> tuple[int, int]:
        """ Получаем размер изображения в зависимости от анимации персонажа """
        return self.__hero[SPRITE_SIZE][self.animation]

    def __set_position_hero(self) -> None:
        """ Устанавливаем начальные координаты персонажа """
        w, h = self.size
        self.x, self.y = self.__w/2 - w/2, self.__h - h

    def __get_position_hero(self) -> tuple[int, int]:
        """ Получаем позицию персонажа на карте """
        w, h = self.size
        # КОСТЫЛЬ: чтобы анимация foxi не искажалась (из сидячего в лежачее состояние);
        SIZE_SLEEP_LEFT = 11*INCREASE if self.__is_flip and MixinAnimationSleep.is_check(self) else 0
        # Координаты персонажа [ x, y ];
        x = self.x - SIZE_SLEEP_LEFT
        y = self.__h-h if MixinAnimationSleep.is_check(self) else self.__h-(h+9)
        return x, y - LEVEL_POSITION_OBJECT

    def set_animation(self, animation: str) -> None:
        """ Установить анимацию для персонажа """
        self.animation = animation

    def flip_hero(self, flip: str) -> None:
        """ Поворот персонажа в зависимости от текущего направления героя """
        if flip == A.LEFT:  # Флаг поворота влево;
            self.set_animation(A.MOVE if self.__is_flip else A.FLIP)
            self.__is_flip = True
        elif flip == A.RIGHT:  # Флаг поворота вправо;
            self.set_animation(A.FLIP if self.__is_flip else A.MOVE)
            self.__is_flip = False

    def move_left(self) -> None:
        """ Движение персонажа влево """
        if MixinAnimationSleep.is_check(self):
            return None
        self.start()  # Обнуляем таймер;
        self.flip_hero(A.LEFT)
        #############################################
        # if self.x >= 0:  # Если не превышает границу слева;
        #     self.x -= self.__speed
        #############################################
        self.x -= self.__speed
        if self.x <= 0 - self.size[0]:  # Если превышает границу слева;
            self.x = self.__w
        #############################################

    def move_right(self) -> None:
        """ Движение персонажа вправо """
        if MixinAnimationSleep.is_check(self):
            return None
        self.start()  # Обнуляем таймер;
        self.flip_hero(A.RIGHT)
        #############################################
        # if self.x <= self.__w - self.size[0]:  # Если не превышает границу справа;
        #     self.x += self.__speed
        #############################################
        self.x += self.__speed
        if self.x >= self.__w:  # Если превышает границу справа;
            self.x = 0 - self.size[0]
        #############################################

    def move_up(self) -> None:
        """ Движение персонажа вверх """
        self.start()  # Обнуляем таймер;
        if MixinAnimationSleep.is_check(self):
            self.set_animation(A.SLEEP_TO_STOP)
        elif MixinAnimationStop.is_check(self):
            self.set_animation(A.MOVE)

    def move_down(self) -> None:
        """ Движение персонажа вниз """
        self.start(4.7)  # Устанавливаем таймер для анимации;
        if MixinAnimationStop.is_check(self) or MixinAnimationMove.is_check(self):
            self.set_animation(A.STOP_TO_SLEEP)
