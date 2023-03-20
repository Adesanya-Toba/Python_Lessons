class Dog:

    # class attribute
    species = "Cannis familiaris" # The same for every instance/object of the class

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # Instance methods
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instead of using the description function, we could use the __str__() to print useful info about the class
    def __str__(self) -> str:
        # This way, when we call print(Dog object), it would output the following
        return f"{self.name} is {self.age} years old"

    
    def speak(self, sound="Woof"):
        return f"{self.name} barks: {sound}"

# Class Inheritance
class BullDog(Dog):
    # speak() here overrides speak in parent class
    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"

class GermanShepherd(Dog):
    # speak() uses the speak in the parent class by with a default argument
    def speak(self, sound="Duff"):
        return super().speak(sound)

    # Alternatively, you could decide to not implement a speak function and automatically use the version in the parent class


def main():
    
    my_dog = Dog("Rudy", 12)

    print(my_dog)
    print(my_dog.description())
    print(my_dog.speak("hello"))

    my_bull_dog = BullDog("Von", 98)
    print(my_bull_dog.speak())

    my_german = GermanShepherd("Holly", 7)
    print(my_german.speak())


if __name__ == "__main__":
    main()