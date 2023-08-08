# Cree una clase Vehículo que contenga los atributos
# de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self, Velocidad_maxima, kilometraje):
        self.Velocidad_maxima = Velocidad_maxima
        self.kilometraje =kilometraje


if __name__ == "__main__":
    carro = Vehiculo(200, 1500)

print("velocidad_maxima: ", carro.Velocidad_maxima)
print("kilometraje: ", carro. kilometraje)





