# Abstract Base Classes are similar to Abstract Classes in C++
# except instead of having a pure virtual function (i.e. func() = 0),
# it inherits the abc.ABC class and decorates functions and properties
# as abstract requiring any subclasses that inherit from it, define those
# function and properties (making them concrete) to be useful.

# The abc.ABC class introduces a metaclass – a class used to build the
# concrete class definitions. Python's default metaclass is named *type*

import abc


class MediaLoader(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...


class Wav(MediaLoader):
    pass


# x = Wav() # Will raise a TypeError as the Wav class has not implemented
# play or ext methods meaning the MediaLoader subclass is still abstract and
# it is impossible to instantiate an abstract class


class Ogg(MediaLoader):
    # This class fills all the placeholders in the MediaLoader class and
    # therefore can instantiate cleanly even if the methods don't do much.
    ext = "ogg"

    def play(self):
        pass


o = Ogg()
