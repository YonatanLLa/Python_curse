# Ejemplo 1: Clase "Persona"

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludar(self):
        print(f"Hola, ma name is {self.nombre} {self.apellido}")

# Crear una instancia de la clase persona
persona1 = Persona("juan", 25)

# Llamar el metodo 'Saludar' de la instancia
persona1.saludar()