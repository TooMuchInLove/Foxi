from dataclasses import dataclass


@dataclass(slots=True)
class IObject:
    """ Интерфейс для любого объекта """
    def get_size(self) -> tuple[int, int]:
        pass

    def draw(self) -> None:
        pass


@dataclass(slots=True)
class ICharacter(IObject):
    """ Интерфейс для любого персонажа """
    def move_left(self) -> None:
        pass

    def move_right(self) -> None:
        pass

    def move_up(self) -> None:
        pass

    def move_down(self) -> None:
        pass


@dataclass(slots=True)
class IStationary(IObject):
    """ Интерфейс для любого неподвижного объекта """
