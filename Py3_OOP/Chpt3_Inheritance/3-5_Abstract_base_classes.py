from collections.abc import Container

class OddContainer:
    '''What we're doing here is classic!
    We find that Container is an abstract base class that
    requires its subclasses to implement its function(s).
    Luckily, Container only has/requires one method:
    __contains__().
    So defining a new class and giving it a function called
    __contains__(), we create an 'is a' relationship between
    the container class and this class, without needing to use
    inheritance.'''
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True
    
odd_container = OddContainer()
print(isinstance(odd_container, Container))
print(issubclass(OddContainer, Container))

print('Using the "in" keyword: ', 1 in odd_container)