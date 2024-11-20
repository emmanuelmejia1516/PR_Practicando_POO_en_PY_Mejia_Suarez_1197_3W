# Ejercicio 7
class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def asignar_carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def mostrar_datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El estudiante {self.nombre} tiene {self.edad} años, está cursando {self.especialidad} en la universidad {self.nombre}")

# Creación de un objeto Estudiante
persona = Estudiante("Universidad Nacional Autónoma de México")
persona.asignar_carrera("Medicina")
persona.mostrar_datos("Carlos", 22)