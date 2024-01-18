import abc
import random
from typing import Type, Set, Iterable


class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"


class D4(Die):
    def roll(self) -> None:
        self.face = random.choice((1, 2, 3, 4))


class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1, 6)


class Dice(abc.ABC):
    def __init__(self, n: int, die_class: Type[Die]) -> None:
        # The type hint is Type[Die], telling mypy to be on the
        # lookout for any subclass of the abstract base class Die.
        # We don't expect an instance of any of the Die subclasses;
        # we expect the class object itself.

        self.dice = [
            die_class for _ in range(n)
        ]  # Creates n number of dice and puts in list

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)


class SimpleDice(Dice):
    def roll(self) -> None:
        for d in self.dice:
            d.roll()


if __name__ == "__main__":
    sd = SimpleDice(6, D6)
    sd.roll()
    print(sd.total)

    d = 0
    # Store the value for d for every increment of d passed over
    d = [d for d in range(4)]
    print(d)

    d = 0
    # Store the same value of d for every for loop iteration.
    d = [d for _ in range(4)]
    print(d)


class YachtDice(Dice):
    def __init__(self) -> None:
        super().__init__(5, D6)
        self.saved: Set[int] = set()

    def saving(self, positions: Iterable[int]) -> "YachtDice":
        if not all(0 <= n < 6 for n in positions):
            raise ValueError("Invalid position")
        self.saved = set(positions)
        return self

    def roll(self) -> None:
        for n, d in enumerate(self.dice):
            if n not in self.saved:
                d.roll()
        self.saved = set()
