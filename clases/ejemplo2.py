# Ejemplo 2: Clase "Rectángulo"

class Rectagulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        print(self.ancho)
        return self.ancho*self.alto
    
    def calcular_perimetro(self):
        return 2*(self.ancho + self.alto)

reactangulo1 = Rectagulo(5,3)

print(reactangulo1.calcular_area())
print(reactangulo1.calcular_perimetro())

