# Raising exceptions
from typing import NoReturn


class EvenOnly(list[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Only integers can be added') # Constructing a TypeError object
        if value % 2 != 0:
            raise ValueError('Only even numbers can be added') # Constructing a ValueError object
        return super().append(value)
    

def main() -> None:
    my_list = EvenOnly()
    # my_list.append('hello')
    my_list.append(2)

    never_returns()


def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

if __name__ == '__main__':
    main()