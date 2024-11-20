# Ejercicio 1
class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 6:
            print("¡Felicidades, aprobaste!")
        else:
            print("Lo siento, no aprobaste.")

# Creando objetos de la clase Estudiante
estudiante1 = Estudiante("Carlos", 4)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Ana", 8)
estudiante2.imprimir()
estudiante2.resultados()