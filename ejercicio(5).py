# Ejercicio 5
class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def mostrar_info(self):
        print(f"La moto tiene {self.llantas} llantas, color {self.color}, precio {self.precio}")

class Carro(Fabrica):
    def mostrar_info(self):
        print(f"El carro tiene {self.llantas} llantas, color {self.color}, precio {self.precio}")

# Creación de objetos Moto y Carro
moto = Moto(2, "Rojo", "$15000")
moto.mostrar_info()

carro = Carro(4, "Azul", "$35000")
carro.mostrar_info()