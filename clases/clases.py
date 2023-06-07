class Persona:
    nombre = ""
    apellido = ""
    edad = ""

# Intancia
# Variable -> objeto


datos = Persona()
datos.nombre = "Yonatan"
datos.apellido = "Llanto aquino"
datos.edad = 23

# print(datos.nombre)

datos1 = Persona()
datos1.nombre = "juan"
datos1.apellido = "chuqui"
datos1.edad = 22

# print(datos1.nombre)

#!!-> Constructor....
# cuando te cargas esto es lo primero que vas hacer
# self: represente a el mismo.
# -> funcion: vive de maner global
# -> metodo: necesita una instacia previa, es una funcion que vive dentro de una clase


class Objeto:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        
    # Metodos
    # Metod de clase
    # Metodo de intancia
    def saludo(self):
        print(f'hola me llamo {self.nombre} {self.apellidos} edad {self.edad}')



# nombre1 = Objeto("Yonatan", "Llanto", 22)
# nombre1.saludo()
# nombre2 = Objeto("juan", "chuqui", 21)
# nombre2.saludo()

class Mascota: 
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.__duenio = "" # Solo se puede acecedor dentro
    
    # Primera Forma
    # getter and setter
    
    # def __getDuenio(self):
    #     return self.__duenio
    
    # def __setDuenio(self, duenio):
    #     self.__duenio = duenio
    
    # duenio = property(__getDuenio, __setDuenio)
    
    #Segunda forma:
    # Decoradores:
    @property
    def duenio(self):
        return self.__duenio
    
    @duenio.setter
    def duenio(self,duenio):
        self.__duenio = duenio
    
    def __metodoPrivado(self):
        print('Hola')
        
    def metodoEncapsulamieto(self):
        self.__metodoPrivado()

# dino = Mascota('Dino', 'Frenchie', 'Vaquita')
# dino.duenio = 'Yonatan'

# print(dino.duenio)

# Poliformismo - Herencia
class Animal:   
    # metodo 
    def hablar(self): 
        pass
    
    def nadar(self):
        pass
    
# Herencia en python
class Perro(Animal):
    def hablar(self): 
        # respuesta
        print("Guau")

class Gato(Animal):
    def hablar(self): 
        # respuesta
        print('Miuuuuuu')