# Ejercicio 2
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
persona = Persona(nombre, edad)
persona.cumpleaños()
persona.cumpleaños()
print(f"{persona.nombre} ahora tiene {persona.edad} años")