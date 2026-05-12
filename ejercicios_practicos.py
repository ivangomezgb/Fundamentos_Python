#EJERCICIO 1
#crear las siguientes variables según su criterio:

#• Una variable que permita almacenar el nombre de una persona.
#• Una variable que permita almacenar un valor de un producto.
#• Una variable que permita almacenar el promedio de una asignatura.
#• Imprima en consola las variables creadas

nombre="Ivan"
producto= 20000
promedio_asignatura= 4.5
print(f"Mi nombre es {nombre} y he comprado un producto con el valor de {producto} el promedio de la asignatura es de {promedio_asignatura}")

#EJERCICIO 2
#Crear programa que lea tipos de datos y los relacione con operadores introducidos por teclado : dos enteros, un float, dos String.

#• Se deben sumar los tres números y se muestran en pantalla.
#• Se debe visualizar el entero mayor.
#• Se debe visualizar el resultado de la división del float con el resto de la división de los dos enteros.
#• Se debe visualizar la concatenación de las dos cadenas leídas.

entero1 = int(input("Ingrese el primer numero entero "))
entero2 = int(input("Ingrese el segundo numero entero "))   
float1 = float(input("Ingrese un numero decimal "))
string1 = input("Ingrese la primera cadena de texto ")
string2 = input("Ingrese la segunda cadena de texto ")
suma = entero1 + entero2 + float1
print(f"La suma de los numeros es : {suma}")
if entero1 > entero2:
    print(f"El numero entero mayor es : {entero1}")
elif entero2 > entero1:
    print(f"El numero entero mayor es : {entero2}")
else:
    print(f"Los numeros enteros son iguales : {entero1} y {entero2}")
division = (entero1 / entero2) / float1
print(f"El resultado de la division del float con el resto de la division de los enteros es : {division}")
concatenacion = string1 + " " + string2
print(f"La concatenacion de las dos cadenas es : {concatenacion}")

print("")

#EJERCICIO 3
#Crear 2 variables enteras, una llamada “Base” y la otra “Exponente”,asignar valores a su criterio. 
#Calcular la potencia utilizando y mostrar el resultado de la operación.

base = int(input("Ingrese la base "))
exponente = int(input("Ingrese el exponente "))
potencia = base ** exponente
print(f"El resultado de la base es {base} elevado al exponente {exponente} es : {potencia}")


#EJERCICIO 4
#Hallar la raíz cuadrada de los siguientes números 2, 8, 9, 27, 28, 55, 121 y mostrar los resultados de cada operación.

numeros = [2, 8, 9, 27, 28, 55, 121]
raiz_2 =  2 ** 0.5
raiz_8 = 8 ** 0.5
raiz_9 = 9 ** 0.5
raiz_27 = 27 ** 0.5
raiz_28 = 28 ** 0.5
raiz_55 = 55 ** 0.5
raiz_121 = 121 ** 0.5
print(f"La raiz cuadrada de 2 es : {raiz_2}")
print(f"La raiz cuadrada de 8 es : {raiz_8}")
print(f"La raiz cuadrada de 9 es : {raiz_9}")
print(f"La raiz cuadrada de 27 es : {raiz_27}")
print(f"La raiz cuadrada de 28 es : {raiz_28}")
print(f"La raiz cuadrada de 55 es : {raiz_55}")
print(f"La raiz cuadrada de 121 es : {raiz_121}")

#EJERCICIO 5
#Crear una variable para almacenar el nombre de un estudiante.
# Crear 5 variables para almacenar 5 diferentes notas decimales.
#Calcular el promedio final del estudiante a partir de las 5 notas decimales. (Recuerda que un promedio se calcula sumando todos los
#valores y dividiendo el resultado por el número de valores). Mostrar el resultado y el nombre del estudiante.

nombre_estudiante = input("Ingrese el nombre del estudiante")
nota1 = float(input("Ingrese la primera nota"))
nota2 = float (input("Ingrese la segunda nota"))
nota3 = float(input("Ingrese la tercera nota"))
nota4 = float(input("Ingrese la cuarta nota"))
nota5 = float(input("Ingrese la quinta nota"))
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"El promedio final del estudiante {nombre_estudiante} es de {promedio}")


#EJERCICIO 6
#Crear una variable entera de nombre “numeroUno” con el valor de 8 y
# una variable entera de nombre “numeroDos” con el valor de 2.
#Intercambiar los valores de ambas variables, de modo que “numeroUno” valga 2, y “numeroDos” valga 8. (Utiliza una variable
# auxiliar). Mostrar los resultados de ambas variables.

numero_Uno = 8
numero_Dos = 2
intercambio = numero_Uno
numero_Uno = numero_Dos
numero_Dos = intercambio
print(f"El valor del numero uno es : {numero_Uno}")
print(f"El valor del numero uno es : {numero_Dos}")

#EJERCICIO 7

#Crear una variable booleana llamada “Estado”. Realizar la siguiente
#operación sobre la variable “Estado”: (5 == 2) || (2 > 1). Mostrar el resultado de la variable “Estado”.

estado = bool((5 == 2)) or bool((2 > 1))
print(f"El resultado de la variable boleana el Estado es {estado}")

#EJERCICIO 8

#• Crear una variable llamada “Resultado”.
#• Dentro de la variable “Resultado”, crear una operación aritmética
#donde se haga uso de todos los operadores matemáticos en
#repetidas ocasiones con los números que tú determines.
#• Ejemplo: (9/2) +8*2/1-(2+2) ....
#• Mostrar el resultado de la operación.

resultado= (9/2) + 8*2/1-(2+2) + 5**3 % 4
print(f"El resultado de la operacion es {resultado}")

#EJERCICIO 9


#• Crear una variable entera llamada “ladoCuadrado” de valor 8 y calcular el área y el
#perímetro del cuadrado a partir de la variable anteriormente creada.
#• Crear una variable entera llamada “baseTriangulo” de valor 9 y una variable
#entera llamada “alturaTriangulo” de valor 8. Crear dos variables enteras llamadas
#“ladoUnoTriangulo” y
#“ladoDosTriangulo” de valor 8 ambas. Calcular el área y el
#perímetro del triángulo a partir de variables anteriormente creadas.
#• Crear una variable entera llamada “baseRectangulo” de valor 8 y una variable
#entera llamada “alturaRectangulo” de valor 6. Calcular el área y el perímetro del
#rectángulo a partir de variables anteriormente creadas.

#CUADRADO
lado_Cuadrado = 8
area_Cuadrado = lado_Cuadrado ** 2
perimetro_Cuadrado = 4 * lado_Cuadrado

#TRIANGULO 
base_Triangulo = 9
altura_Triangulo = 8

lado_Uno_Triangulo = 8
lado_Dos_Triangulo = 8

area_Triangulo = (base_Triangulo * altura_Triangulo) / 2
perimetro_Triangulo = base_Triangulo + lado_Uno_Triangulo + lado_Dos_Triangulo

#RECTANGULO 
base_rectangulo = 8
altura_rectangulo = 6

area_rectangulo = base_rectangulo * altura_rectangulo
perimetro_Rectangulo = 2 * (base_rectangulo + altura_rectangulo)
print(f"El area del cuadrado es : {area_Cuadrado} y el perimetro del cuadrado es : {perimetro_Cuadrado}")
print(f"El area del triangulo es : {area_Triangulo} y el perimetro del triangulo es : {perimetro_Triangulo}")
print(f"El area del rectangulo es : {area_rectangulo} y el perimetro del rectangulo es : {perimetro_Rectangulo}")



#EJERCICIO 10

#Desarrollar un programa que permita por medio de la edad de una persona,
#determinar la categoría en la que pertenece a raíz de la siguiente tabla:

#• Rango de edad Categoría
#• 0 - 5 Infante
#• 6 - 10 Niño
#• 11 - 15 Pre adolescente
#• 16 - 18 Adolescente
#• 19 - 25 Pre adulto
#• 26 - 40 Adulto
#• 41 - 55 Pre anciano
#• 56+ Anciano


edad = int(input("Ingrese la edad de la persona: "))

if edad >= 0 and edad <= 5:
    print("Categoría: Infante")

elif edad >= 6 and edad <= 10:
    print("Categoría: Niño")

elif edad >= 11 and edad <= 15:
    print("Categoría: Pre adolescente")

elif edad >= 16 and edad <= 18:
    print("Categoría: Adolescente")

elif edad >= 19 and edad <= 25:
    print("Categoría: Pre adulto")

elif edad >= 26 and edad <= 40:
    print("Categoría: Adulto")

elif edad >= 41 and edad <= 55:
    print("Categoría: Pre anciano")

elif edad >= 56:
    print("Categoría: Anciano")

else:
    print("Edad no válida")