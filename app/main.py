from abc import ABC


class IntegerRange:
    def __init__(
            self,
            min_amount: int,
            max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(
            self,
            owner: type,
            name: str) -> None:
        self.protected_name = "_" + name

    def __get__(
            self,
            instance: None | object,
            owner: type):
        return getattr(instance, self.protected_name)

    def __set__(
            self,
            instance: None | object,
            value: int) -> int:
        if not isinstance(value, int):
            raise TypeError()
        if self.min

    class Visitor:


pass


class SlideLimitationValidator(ABC):
    pass


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    pass


class AdultSlideLimitationValidator(SlideLimitationValidator):
    pass


class Slide:
    pass
