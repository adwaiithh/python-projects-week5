from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a Rectangle")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a Triangle")


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    shape.draw()
    print("Area:", shape.area())
    print("----------------------")