from time import time
from typing import Callable


class GameTimer:
    """ Таймер для анимации объектов """
    __slots__ = ("__begin",)

    def __init__(self) -> None:
        self.__begin = time() # Начальное время для отсчёта

    def start(self, current_time: float = 0.0) -> None:
        """ Установить таймер """
        self.__begin = time() if current_time == 0.0 else current_time

    def tick(self, action: Callable, command: str | int) -> None:
        """ Таймер для отслеживания состояния персонажа """
        end = time() - self.__begin
        if end >= 5.0:
            action(command)
        elif end >= 4.7:
            action(command)
        elif end >= 0.2:
            action(command)
