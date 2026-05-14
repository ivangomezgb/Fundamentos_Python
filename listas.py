#Listas
#ESTRUCTURA LISTA

#INDICE 0    0            1            2
from re import A


lista = ["objeto_1" , "objeto_2", "objeto_3"]
print(type(lista))

listas_mixta = ["Hola", 123 , 3.14, True , [1,2,3]]
print(type(listas_mixta))



#Lista de aprendices SENA ADSO

#CREAR UNA LISTA VACIA
#Indice         0       1       2           3         4       5         6      7
#Indice negativo -8      -7      -6          -5        -4      -3        -2     -1
aprendices =   ["Leo", "Juan", "Carlos", "Sthepani", "Luis","Julian", "Laura","Jhon"]
print (aprendices)

#Accede a un elemento de la lista por el indice siempre se inicia de 0
print (aprendices[4])

#Modificar un elemento de la lista por el indice
aprendices[2] = "Camilo"
print(aprendices)

#Consultar rangos de los elementos de la lista 

print(aprendices[0:2]) #El rango se inicia de 0 y se detiene antes del indice 2 no se toma el indice 2 (solo se toma el indice 0 y 1)
print(aprendices[:3])
print(aprendices[3:6])
print(aprendices[0:3:6])
print(aprendices[-5:-1])

aprendices_ficha_3321349 = ["Leo", "Juan", "Carlos", "Sthepani", "Luis","Julian", "Laura","Jhon"]
aprendices_ficha_2993648 = ["Camilo", "Sofia", "Valentina", "Andres", "Maria", "Diego", "Sara", "David"]

#Concatenar dos listas
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_2993648
print(aprendices_adso)


#Unir listas con extend
aprendices_adso.extend(aprendices_ficha_2993648 + aprendices_ficha_3321349)
print(aprendices_adso)

#Medir con len la cantidad de los elementos de la lista
print(len(aprendices_adso))
print(f"En la lista de aprendices hay {len(aprendices_adso)} elementos")

#Contar elementos repetidos con count 
print(aprendices_adso.count("Leo"))
print(f"El nombre Leo se encuentra {aprendices_adso.count('Leo')} veces en la lista")

#Obtener el indice de un elemento con index
print(aprendices_adso.index("Camilo"))
print(f"El nombre Camilo se encuentra en el indice {aprendices_adso.index('Camilo')} de la lista")

#Copiar una lista con copy
aprendices_adso_copia = aprendices_adso.copy()
print(f"La copia de la lista de aprendices tiene {len(aprendices_adso_copia)} elementos")

#Agregar elementos ala lista con append e insert
aprendices_adso_copia.append("Sofia")
print(f"La copia de la lista de aprendices tiene {len(aprendices_adso_copia)} elementos")

#Insert un elemento en un indice especifico con insert
aprendices_adso_copia.insert(2,"Valentina")
print(f"Valentina se encuentra en el indice {aprendices_adso_copia.index('Valentina')} de la lista")

# Elimnar elementos con remove y pop
aprendices_adso_copia.remove("Sofia")
print(f"Eliminamos el nombre {aprendices_adso_copia.remove('Sofia')} de la lista de aprendices")

# Pertinnencia de un elemento con in
print("Leo" in aprendices_adso_copia)
print("Lei" in aprendices_adso_copia)

#sort ordenar los elementos de la lista
aprendices_adso_copia.sort()#Ordena los elementos de la lista de forma alfabetica
print(aprendices_adso_copia)


#REVERSE invertir el orden de los elementos de la lista
aprendices_adso_copia.reverse()
print(aprendices_adso_copia)


#clear eliminar todos los elementos de la lista
aprendices_adso_copia.clear()
print(aprendices_adso_copia)
