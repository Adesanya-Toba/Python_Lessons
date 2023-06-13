from math import hypot
from typing import Tuple, List, Optional, Iterable

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def distance(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)


class Polygon:
    def __init__(self) -> None:
        self.vertices: List[Point] = []

    def add_point(self, point: Point) -> None:
        self.vertices.append((point))

    def perimeter(self) -> float:
        pairs = zip(
        self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)
    
class Polygon2:
    def __init__(self, vertices: Optional[Iterable[Point]]=None) -> None:
        self.vertices = list(vertices) if vertices else []

    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)


if __name__ == '__main__':
    var1 = (1, 2, 3)
    var2 = ('a', 'b', 'c', 'd', 'e')

    print(var2[2:]) # print everything from the 2th element
    print(var2[:3]) # print the first 3 items in the list

    result = zip(var1, var2)
    print(set(result))