# Ejercicio 4
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_nombre_completo(self):
        print(f"{self.nombre} {self.apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera

    def mostrar_carrera(self):
        print(f"Carrera: {self.carrera}")

# Creación de un objeto Estudiante
estudiante1 = Estudiante("Lucía", "Gómez", "Arquitectura")
estudiante1.mostrar_nombre_completo()
estudiante1.mostrar_carrera()