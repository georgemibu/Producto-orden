from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = productos if productos is not None else []


    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ' / '.join(str(producto) for producto in self._productos)
        return f'Orden: {self._id_orden}, Productos: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto("zapato" , 200.00)
    producto2 = Producto("camisa" , 150.00)

    
