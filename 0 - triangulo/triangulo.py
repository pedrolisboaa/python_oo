from math import sqrt


class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self._lado_a = lado_a
        self._lado_b = lado_b
        self._lado_c = lado_c

    def area(self):
        p = (self._lado_a + self._lado_b + self._lado_c) / 2
        area = sqrt(p * (p - self._lado_a) * (p - self._lado_b) * (p - self._lado_c))
        return area
