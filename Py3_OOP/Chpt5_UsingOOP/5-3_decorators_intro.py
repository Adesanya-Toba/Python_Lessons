#  Decorators modify the function definition that they precede.
class NorwegianBlue_P:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str

    @property
    def silly(self) -> str:
        """Docstring for silly property."""
        print(f"Getting {self._name}'s state:", end=" ")
        return self._state

    @silly.setter
    def silly(self, state: str):
        print(f"Setting {self._name}'s state to {state!r}")
        self._state = state

    @silly.deleter
    def silly(self):
        print(f"{self._name} is getting deleted!")
        del self._state


def main():
    p = NorwegianBlue_P("Polly")
    p.silly = "Pinning for the fjords"
    print(f"{p.silly!r}")
    del p.silly

    print("hello")


if __name__ == "__main__":
    main()
