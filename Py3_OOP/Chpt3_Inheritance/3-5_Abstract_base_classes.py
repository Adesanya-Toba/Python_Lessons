import abc
from collections.abc import Container


class OddContainer:
    """What we're doing here is classic!
    We find that Container is an abstract base class that
    requires its subclasses to implement its function(s).
    Luckily, Container only has/requires one method:
    __contains__().
    So defining a new class and giving it a function called
    __contains__(), we create an 'is a' relationship between
    the container class and this class, without needing to use
    inheritance."""

    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True


odd_container = OddContainer()
print(isinstance(odd_container, Container))
print(issubclass(OddContainer, Container))

print('Using the "in" keyword: ', 1 in odd_container)


# Create an Abstract Base Class
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # Python decorator. Because it's marked as abstract, this
    # means that any subclass must implement this method
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod  # Meaning this method can be called on a Class instead of an
    # instantiated object.
    def __subclasshook__(cls, C):
        """This says that any class that supplies the concrete implementations of
        all the attributes of this ABC should be considered a subclass of
        MediaLoader, even if it doesn't actually inherit from MediaLoader.
        """
        if cls is MediaLoader:
            attrs = set(
                dir(C)
            )  # Get a set of methods and props in this class including any parent
            # classes and hierarchy
            if set(cls.__abstractmethods__) <= attrs:
                """Using set notation to check if the methods have been implemented in
                this class"""
                return True

        return NotImplemented


# Testing these new functions and constructs
attrs = set(dir(MediaLoader))
print(attrs)
print("\n")
print(set(MediaLoader.__abstractmethods__))


class Wav(MediaLoader):
    pass


class Ogg(Wav):
    ext = ".ogg"

    def play(self):
        pass


class DecoratorTest:
    @classmethod
    def decor_print(cls):
        print("Printing directly from class DecoratorTest")

    def another_func(self):
        print("Printing from a non-class method.")

    @staticmethod
    def stat_func():
        """
        This works without the staticmethod decorator
        but we should add it for type checking.

        It doesn't really do much and isn't super useful it just says the
        function is closely related to this class even though it doesn't
        use any of the class attributes.

        It works just like a regular function and could have easily been defined
        outside of the class.
        """
        print("Printing from a static method")


# x = Wav() # Will not work because the Wav class doesn't implement play() or ext
y = Ogg()

DecoratorTest.decor_print()
# DecoratorTest.another_func() # Does not work.
DecoratorTest.stat_func()

# Only works with objects of class DecoratorTest
dec = DecoratorTest()
dec.another_func()
