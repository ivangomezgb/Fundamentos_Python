#Tuplas 

#Estructura de una tupla

tupla = ("Elemento1","Elemento2", "Elemento3")
print(type(tupla)) # CLASE TUPLE

#Segunda forma de crear una tupla
tupla = "Hola1" , "Hola2", "Hola3"
print(type(tupla)) # CLASE TUPLE

#Tupla de aprendices ADSO

# Indices       0      1        2        3
aprendices = ("Leo","David","Daniel","Julian")
print(aprendices)

# Acceder al elementos de la tupla
print(aprendices[2]) # DANIEL

# Modificar elementos de tupla 
# aprendices[2] = "Daniel" esto generara un error por que las tuplas son inmutables

#Consultar rangos de elementos de la tupla
print(aprendices[0:2]) 
print(aprendices[2:4]) 
print(aprendices[1:])

#Suma 2 tuplas 

tupla_1 = (1,2,3)
tupla_2 = (4,5,6)
tupla_suma = tupla_1 + tupla_2
print(tupla_suma)

#Multiplicar una tupla
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada)


# Metodos de tuplas 

# Medir el largo con len()
print(len(aprendices))

# Contar elementos repetidos en una tupla con count
print(aprendices.count("Leo")) 

#Obtener  el indice de un elemento con index
print(aprendices.index("Julian"))

# Modificar una tupla en una lista 
print(type(aprendices)) #tuple
aprendices = list(aprendices)
aprendices.append("Leo")
print(type(aprendices))
print(aprendices)

aprendices = tuple(aprendices)
print(type(aprendices))

# Comprobar permanencia con in 
print("Leo" in aprendices)
print("Julian" in aprendices)

# Empaquetar y desempaquetar tuplas 

#Empaquetar tupla
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "TOPOGRAFIA"

tupla_empaquetada = programa_1 , programa_2 , programa_3
print(tupla_empaquetada)

#Desempaquetar tuplas
tupla_desempaquetada = ("ADSO","SST","TOPOGRAFIA")
programa_1,programa_2,programa_3 = tupla_desempaquetada
print(programa_1)
print(programa_2)
print(programa_3)

#Ejercicio 2 desempaquetar tupla
tupla_ciudades = ("BOGOTA","VILLAVICENCIO","MEDELLIN")
ciudad_1, * ciudad_2 = tupla_ciudades
print(ciudad_1)
print(ciudad_2) 

# Ejerccio 1) Almacen de vectores 

vector_1 = (1,2,3) 
vector_2 = (-1,0,2)

# Suma
producto_escalar = vector_1 + vector_2
print(sorted(producto_escalar))

# Ejerccio 2) Almacen de precios
precios = 50, 75, 46, 22, 80, 65, 8,

print("El precio menor es :",min(precios))
print("El precio mayor es :",max(precios))