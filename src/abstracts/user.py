from abc import ABC, abstractmethod


class AbstractWindow(ABC):
    @abstractmethod
    def screen_blit(self) -> None:
        pass

    @abstractmethod
    def form_update(self) -> None:
        pass

    @abstractmethod
    def size(self) -> tuple[int, int]:
        pass
