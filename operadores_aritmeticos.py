
# Operadores aritméticos #

from math import pi


a = 5
b = 2


suma = a + b
print(f"La suma de {a} y {b} es : {suma}")

resta = a -b 
print(f"La resta de {a} y {b} es : {resta}")

multiplicacion = a * b
print(f"La multplicacion de {a} y {b} es : {multiplicacion}")

division = a / b
print(f"La division de {a} y {b} es : {division}")

#modulo o residuo
residuo = a % b 
print(f"El modulo de {a} entre {b} es : {residuo}")

#potencia o exponenciacion
potencia = a ** b
print(f"{a} elevado a la {b} es : {potencia}")

#precedencia de operadores 
resultado_1 = a + b * 2
print(f"El resultado1 de la operacion {a} + {b} * 2 es : {resultado_1}")

resultado_2 = (a + b) * 2
print(f"El resultado2 de la operacion {a} + {b} * 2 es : {resultado_2}")

resultado_3 = a * b * 3
print(f"El resultado3 de la operacion {a} + {b} * 3 es : {resultado_3}")

resultado_4 = (a + b) * 3
print(f"El resultado4 de la operacion {a} + {b} * 3 es : {resultado_4}")

resultado_5 = a / b * 4
print(f"El resultado5 de la operacion {a} + {b} * 4 es : {resultado_5}")

resultado_6 = (a + b) * 4
print(f"El resultado6 de la operacion {a} + {b} * 4 es : {resultado_6}")


#Librerias de Matematicas

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


import random 

random.random()
numero_ale=random.randint(1, 100)
print(numero_ale)