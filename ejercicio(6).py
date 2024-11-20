# Ejercicio 6
class Marino():
    def hablar(self):
        print("Hola, soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un Pulpo!")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)

# Creación de objetos Marino, Pulpo y Foca
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca!")