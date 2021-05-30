'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

    def rectangle_perimeter(self):
        return (self.length + self.width) * 2

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * (self.radius ** 2)

    def circle_circum(self):
        return 2 * math.pi * self.radius

rect_ = Rectangle(10, 2)
circ_ = Circle(5)
print(f"Rectangle area is {rect_.rectangle_area()} and the perimeter is {rect_.rectangle_perimeter()}")
print(f"Circle area is {circ_.circle_area()} and the circumpherence is {circ_.circle_circum()}")