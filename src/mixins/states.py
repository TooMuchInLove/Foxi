from config import Action as A


class MixinAnimationSleep:
    """ Миксин: состояние покоя объекта. """
    def is_check(self) -> bool:
        if self.animation == A.SLEEP:
            return True
        return False


class MixinAnimationStop:
    """ Миксин: состояние остановки объекта. """
    def is_check(self) -> bool:
        if self.animation == A.STOP:
            return True
        return False


class MixinAnimationMove:
    """ Миксин: состояние движения объекта. """
    def is_check(self) -> bool:
        if self.animation == A.MOVE:
            return True
        return False
