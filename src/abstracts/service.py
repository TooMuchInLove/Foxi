from abc import ABC, abstractmethod


class AbstractObject(ABC):
    """ Абстракция для любого объекта """
    @abstractmethod
    def timer(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def size(self) -> tuple[int, int]:
        pass


class AbstractCharacter(AbstractObject):
    """ Абстракция для любого персонажа """
    @abstractmethod
    def move_left(self) -> None:
        pass

    @abstractmethod
    def move_right(self) -> None:
        pass

    @abstractmethod
    def move_up(self) -> None:
        pass

    @abstractmethod
    def move_down(self) -> None:
        pass


class AbstractStationary(AbstractObject):
    """ Абстракция для любого неподвижного объекта """
