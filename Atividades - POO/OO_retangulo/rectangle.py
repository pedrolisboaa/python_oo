from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def diagonal(self):
        return sqrt((self.height ** 2) + (self.width ** 2))