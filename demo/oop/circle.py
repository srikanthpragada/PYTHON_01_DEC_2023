import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        print(f"{self.x},{self.y} - {self.r}")

    def area(self):
        return math.pi * self.r * self.r


c1 = Circle(10, 20, 15)
print(c1.area())
c2 = Circle(10, 10, 20)
print(c2.area())
