import math
from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def show(self):
        super().show()
        print(self.r)

    def area(self):
        return math.pi * self.r * self.r


class Rectangle(Shape):
    def __init__(self, x, y, l, w):
        super().__init__(x, y)
        self.l = l
        self.w = w

    def show(self):
        super().show()
        print(self.l)
        print(self.w)

    def area(self):
        return self.l * self.w


s = Shape(10, 20)

c = Circle(10, 20, 15)
c.show()
print(c.area())

r = Rectangle(10, 10, 10, 20)
r.show()
print(r.area())


shapes = []
