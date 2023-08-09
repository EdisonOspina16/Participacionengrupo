import math


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def contiene_punto(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio


c = Circulo((0, 0), 5)
print(c.area())
print(c.perimetro())
print(c.contiene_punto((3, 4)))
print(c.contiene_punto((6, 7)))
