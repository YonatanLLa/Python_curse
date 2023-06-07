# Ejercicio: Clase "Banco"

class Banco: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
    
    
    def agregar_cliente(self, cliente):
        if cliente.id not in self.clientes:
            self.clientes[cliente.id] = cliente
        
        else:
            print(f"El cliente con el ID {cliente.id} ya existe en el banco.")
            
    def remover_cliente(self, id_cliente):
        if id_cliente in self.clientes:
            del self.clientes[id_cliente]
        else:
            print(f"No se encontró el cliente con ID {id_cliente} en el banco")

# Clase Cliente 
class Cliente:
    def __init__(self, nombre):
        self.id = id
        self.nombre = nombre

#Crear una instancia de la clase Cliente
banco = Banco("Mi banco")

# Crear instancia de la clase cliente
cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "yonatan")
cliente3 = Cliente(3, "Pedro")

# Agregar clientes al banco 
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)
banco.agregar_cliente(cliente3)

# Listar los clientes en el banco
banco.listar_clientes()

banco.remover_cliente(3)

banco.listar_clientes()