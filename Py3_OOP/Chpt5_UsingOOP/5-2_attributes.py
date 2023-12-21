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
        """Get color name"""
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


class NorwegianBlue:
    def __init__(self, name) -> None:
        self._name = name
        self._state: str

    def test_method(self):
        """Test method"""
        pass

    def _get_state(self):
        """This is the get method for class NorwegianBlue.
        If no docString is provided in the property description,
        the docstring in the getter method is used.
        """
        print(f"Getting {self._name}'s state")
        return self._state

    def _set_state(self, state: str):
        print(f"Setting {self._name}'s state to {state!r}")
        self._state = state

    def _del_state(self):
        print(f"{self._name} is pushing up daisies!")
        del self._state

    silly = property(_get_state, _set_state, _del_state)


def main():
    c = Color(0xFF0000, "bright red")
    print(c.name)
    c._set_name("red")  # Shouldn't call private methods
    print(c._get_name())

    # Setting attributes directly using properties
    c.name = "Black"
    try:
        c.name = ""  # Raises a ValueError because this operation goes through the
    except ValueError:
        print("Expected value error.")
    # property (_set_name) setter function which performs input validations.
    print(c.name)  # Works as well

    p = NorwegianBlue("Polly")
    p.silly = "Pinning for the fjords"
    print(p.silly)
    del p.silly

    print("hello")


if __name__ == "__main__":
    main()
