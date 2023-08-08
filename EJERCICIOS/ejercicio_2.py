# 2. Cree una clase Punto que represente un punto en el plano cartesiano.

# 3. A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
import math


class Punto:
    def __init__(self,x:str , y: str):
        self.x = x
        self.y = y

    def mostar(self):
        print("coordenadas: ", self.x ",", self.y)

if __name__ == "__main__":
    Punto = Punto(16, 20)

    def mover(self,nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x,otro_punto.x)**2 +(self.y, otro_punto.y)**2)

 print("punto_X: ", Punto.x)
 print("punto_Y: ", Punto.y)




