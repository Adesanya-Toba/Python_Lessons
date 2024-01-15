from collections.abc import Container


class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0


odd = OddIntegers()
# The two lines below return True due to Duck Typing as it creates a
# is-a relationship without the overhead of writing the code to set up
# inheritance.
print(isinstance(odd, Container))
print(issubclass(OddIntegers, Container))

# The Container class provides the "in" keyword as syntax sugar for the
# __contains__() method.
print(1 in odd)
print(2 in odd)
