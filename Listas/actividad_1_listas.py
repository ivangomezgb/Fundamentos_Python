productos = ["Lapiz", "Cuaderno", "Borrador", "Regla", "Colores"]
precios = [1000, 3500, 500, 1500, 6000]

cantidades = [10, 20, 14, 12, 8]

print(" Inventario de la tienda escolar:"
      "\n productos: ", productos,
        "\n precios: ", precios,
    "\n cantidades: ", cantidades
      )

print(f"El producto {productos[0]} tiene un precio de {precios[0]} pesos con una cantidad de {cantidades[0]} unidades disponible en el inventario")
print(f"El producto {productos[1]} tiene un precio de {precios[1]} pesos con una cantidad de {cantidades[1]} unidades disponible en el inventario")
print(f"El producto {productos[2]} tiene un precio de {precios[2]} pesos con una cantidad de {cantidades[2]} unidades disponible en el inventario")
print(f"El producto {productos[3]} tiene un precio de {precios[3]} pesos con una cantidad de {cantidades[3]} unidades disponible en el inventario")
print(f"El producto {productos[4]} tiene un precio de {precios[4]} pesos con una cantidad de {cantidades[4]} unidades disponible en el inventario")

print(type(productos)) # <class 'list'>
print(type(productos[1])) # <class 'str'>
print(type(productos[2])) #<class 'str'>
print(type(productos[3])) #<class 'str'>
print(type(productos[4])) #<class 'str'>




