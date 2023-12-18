class Color:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name:
            raise ValueError(f"Invalid name {name!r}")
        self._name = name

    def _set_name(self, name: str) -> None:
        if not name:
            raise ValueError(f"Invalid name {name!r}")
        self._name = name

    def _get_name(self) -> str:
        return self._name

    def set_rgb_value(self, rgb_value: int):
        self._rgb_value = rgb_value

    def get_rgb_value(self) -> int:
        return self._rgb_value

    # Add a 'property' attribute to create a new attribute that enforces the functions
    # we pass as parameters. i.e., When used in an access context (on the right
    # side of the = or :=), the first function gets the value. When used in an update
    # context (on the left side of = or :=), the second function sets the value
    name = property(_get_name, _set_name)


def main():
    c = Color(0xFF0000, "bright red")
    print(c.name)
    c._set_name("red")  # Shouldn't call private methods
    print(c._get_name())

    # Setting attributes directly using properties
    c.name = "Black"
    # c.name = ""  # Raises a ValueError
    print(c.name)  # Works as well


if __name__ == "__main__":
    main()
