# Ejemplo 3: Clase "Calculadora"
class Calculadora:
    def __init__(self):
        self.resultado = 0
        
    def sumar(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b != 0:
            return a/b
        else:
            print("No se puede dividir entre 0")

calculadora1 = Calculadora()

print(calculadora1.sumar(12, 4))
print(calculadora1.resta(12, 10))
print(calculadora1.multiplicar(5, 8))
print(calculadora1.dividir(6, 0))