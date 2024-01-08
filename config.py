# from enum import Enum
from dataclasses import dataclass

# Ставим игру на паузу;
isPAUSE = False
# Запуск игры;
isGAME = True
# Вызов меню игры;
isMENU = True

# Отрисовка каждые 0.1 сек;
FPS = 100
# Увеличиваем объекты в X раз(а);
INCREASE = 3
# Расположение объекта на уровне N
LEVEL_POSITION_OBJECT = 20
# 290x130, 250x112, 200x90
# Ширина/Высота рабочего окна;
WIDTH = 290 * INCREASE
HEIGHT = 130 * INCREASE
# Название игры
TITLE = "Little fox Foxy"
# Расположение изображений;
DIR_IMG = "imgs"
# Ключ для определения размера спрайтов
SPRITE_SIZE = "size"

# ПУНКТЫ МЕНЮ ПРИ ЗАПУСКЕ ПРИЛОЖЕНИЯ;
LIST_MENU = (
    (0, 'Foxi'),
    (1, 'Start game'),
    (2, 'Exit game'),
    (3, 'Test'),
    (4, 'Test'),
)


@dataclass(slots=True, frozen=True)
class Action:
    """ Набор действия и состояний персонажа """
    RIGHT = "->"  # Движение вправо;
    LEFT = "<-"  # Движение влево;
    MOVE = "move"  # Движение;
    STOP = "stop"  # Сидячее положение;
    FLIP = "flip"  # Разворот;
    SLEEP = "sleep"  # Спит;
    STOP_TO_SLEEP = "stop_to_sleep"  # Из сидячего положения в стоячее;
    SLEEP_TO_STOP = "sleep_to_stop"  # Из стоячего положения в сидячее;


@dataclass(slots=True, frozen=True)
class Palette:
    """ Палитра цветов для """
    LIGHT_GREEN = (0, 200, 0) # Цвет: ярко-зелёный
    GLOOMY_GREY = (153, 154, 153) # Цвет: хмуро-серый
    BLACK_GREY = (26, 26, 26) # Цвет: тёмно-серый
    LIGHT_BROWN = (153, 102, 52) # Цвет: светло-коричневый
    DARK_BROWN = (101,  51, 0) # Цвет: тёмно-коричневый
    WHITE = (255, 255, 255) # Цвет: белый
    BLACK = (0, 0, 0) # Цвет: чёрный
    YELLOW = (250, 239, 4) # Цвет: жёлтый


# Временное хранилище для изображений;
SPRITES = {
    "fox": {
        "path": f"{DIR_IMG}/fox",
        "sprites": {
            Action.MOVE: (39*INCREASE, 33*INCREASE),
            Action.SLEEP: (48*INCREASE, 19*INCREASE),
            Action.STOP: (39*INCREASE, 33*INCREASE),
            Action.FLIP: (39*INCREASE, 33*INCREASE),
            Action.STOP_TO_SLEEP: (39*INCREASE, 33*INCREASE),
            Action.SLEEP_TO_STOP: (39*INCREASE, 33*INCREASE),
        },
    },
    "heal": {
        "path": f"{DIR_IMG}/top_panel",
        "sprites": {
            "heal": (7*INCREASE, 6*INCREASE),
            "energy": (7*INCREASE, 6*INCREASE),
        },
    },
    "bush": {
        "path": f"{DIR_IMG}/bush",
        "sprites": {
            "bush": (75*INCREASE, 77*INCREASE),
        },
    },
    "BTN": {
        "path": f"{DIR_IMG}/btn",
        "sprites": {
            "bg": (8*INCREASE, 8*INCREASE),
            "help": (8*INCREASE, 8*INCREASE),
            "help1": (8*INCREASE, 8*INCREASE),
            "help2": (8*INCREASE, 8*INCREASE),
            "left": (12*INCREASE, 9*INCREASE),
            "ok": (12*INCREASE, 9*INCREASE),
            "right": (12*INCREASE, 9*INCREASE),
            "close": (12*INCREASE, 9*INCREASE),
        },
    },
}
