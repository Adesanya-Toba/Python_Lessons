# Dataclasses are like regular classes except they come with some
# automatically generated special methods such as __init__(), __repr__()
# and __eq()__ to regular classes.
# It also allows two dataclasses to compared based on their attributes

from dataclasses import dataclass
from time import time


@dataclass
class Position:
    name: str
    lon: float
    lat: float = 20.1


pos = Position("Landmark", 19.2)
print(pos)
print(pos.lat)

pos2 = Position("Landmark", 19.2)

print(pos == pos2)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.get("price")
x = car["price"]

print(x)
print(car)
