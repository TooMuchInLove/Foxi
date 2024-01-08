from time import time
from typing import Callable
from dataclasses import dataclass
from objects import IObject


@dataclass(slots=True)
class Action:
    """ Временное хранилище для действий над объектами """
    sec: float
    action: Callable
    command: str


class GameTimer:
    """ Таймер для анимации объектов """
    __slots__ = ("__list_actions", "__begin",)

    def __init__(self) -> None:
        # # Список действий над объектом
        # self.__list_actions = []
        # Начальное время для отсчёта
        self.__begin = time()

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

    # def start(self, timer) -> bool:
    #     # self.__begin = time()
    #     end = time() - self.__begin
    #     # print(end)
    #     if end >= timer:
    #         return False
    #     return True
    #
    # def add_action(self, sec: float, action: Callable, command: str) -> None:
    #     # self.__list_actions.append((_sec, _action, _command))
    #     self.__list_actions.append(
    #         Action(sec=sec,
    #                action=action,
    #                command=command)
    #     )
    #
    # def check(self) -> None:
    #     end = time() - self.__begin
    #     for i, obj in enumerate(self.__list_actions):
    #         if end >= obj.sec:
    #             obj.action(obj.command)
    #             self.__list_actions.pop(i)
    #
    # def restart(self) -> None:
    #     pass
    #
    # def cancel(self) -> None:
    #     pass


# def get_action(msg: str) -> None:
#     print(msg)


# START = True
# t = Timer()
# t.add_action(0.2, get_action, "stop")
# t.add_action(4.7, get_action, "stop_to_sleep")
# t.add_action(5, get_action, "sleep")
# while START:
#     START = t.start(10)
#     t.check()
