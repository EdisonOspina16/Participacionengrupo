class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


    def mostrar_datos(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {self.propietarios}")
        print(f"Balance: {self.balance}")
