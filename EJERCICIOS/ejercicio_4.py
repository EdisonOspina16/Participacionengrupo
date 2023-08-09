class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def perimetro(self):
        longitud = abs(self.p2[0] - self.p1[0])
        ancho = abs(self.p2[1] - self.p1[1])
        return (longitud + ancho) * 2

    def area(self):
        longitud = abs(self.p2[0] - self.p1[0])
        ancho = abs(self.p2[1] - self.p1[1])
        return longitud * ancho

    def es_cuadrado(self):
        longitud = abs(self.p2[0] - self.p1[0])
        ancho = abs(self.p2[1] - self.p1[1])
        return longitud == ancho


r = Rectangulo((0, 0), (4, 3))
print(r.perimetro())
print(r.area())



