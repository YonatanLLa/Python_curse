# Ejercicio: Clase "Tienda"

class Tienda: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        
    def agergar_producto(self, producto):
        self.productos.append(producto)
    
    def remove_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"El producto {producto} no existe en la tienda")
    
    def listar_productos(self):
        print(f"Productos en la tienda {self.nombre}")
        for index, producto in enumerate(self.productos):
            print(f"N{index + 1}: {producto}")


# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self) -> str:
        return f"{self.nombre} - {self.precio}$"

# Crear una instacioa de la tiena
tienda = Tienda("Mi Tienda")

# Crear instancia de la clase Producto

producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

# Agregar productos a la tienda
tienda.agergar_producto(producto1)
tienda.agergar_producto(producto2)
tienda.agergar_producto(producto3)
producto4 = "Laptop"
# Listar los productos en la tienda
tienda.listar_productos()

# Remover un producto de la tienda 
tienda.remove_producto(producto4)


