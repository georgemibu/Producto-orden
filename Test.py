from Producto import Producto
from Orden import Orden


producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 159.00)
producto3 = Producto ("Pulsera", 40.00)

productos1 = [producto1,producto2]
productos2 = [producto3]

orden1 = Orden(productos1)

orden1.agregar_producto(producto3)
print(orden1)
orden2 = Orden(productos2)

print(f'Total orden 1: {orden1.calcular_total()}')
print(f'Total orden 2: {orden2.calcular_total()}')