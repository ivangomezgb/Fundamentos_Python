#Listas
#ESTRUCTURA LISTA

#INDICE 0    0            1            2
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
print(aprendices_ficha_3321349 + aprendices_ficha_2993648)
