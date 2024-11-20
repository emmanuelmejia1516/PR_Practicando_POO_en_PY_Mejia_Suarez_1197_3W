# Ejercicio 3
class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        resultado = self._num1 / self._num2
        print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

# Creación de objetos de la clase Calculadora para cada operación
operacion = Calculadora(12, 6)
operacion.suma()

operacion = Calculadora(15, 3)
operacion.resta()

operacion = Calculadora(30, 5)
operacion.division()

operacion = Calculadora(7, 9)
operacion.multiplicacion()