# Variables de diferentes tipos de datos #

nombre = "Leito"
apellido = "Gomez"
edad = 19
altura = 1.70
activo = True
correo = "ivanleongomez2012@gmail.com"
telefono = "3142794173"
cedula = 1234567890

# Convertir las variables a los tipos de datos correspondientes #
telefono_int = int(telefono)
edad_float = float(edad)
edad_float = float(edad)
altura_int = int(altura)
cedula_string = str(cedula)

# Imprimir el tipo de dato y el valor de cada variable #
print(type(nombre), (nombre))
print(type(apellido), (apellido))
print(type(edad), (edad))
print(type(activo), (activo))
print(type(correo), (correo))
print(type(telefono_int), (telefono_int))
print(type(edad_float), (edad_float))
print(type(edad_float), (edad_float))
print(type(altura_int), (altura_int))
print(type(cedula_string), (cedula_string))

# Comentarios en Python

"""
Este es un comentario de varias líneas en Python.
Puedes usarlo para explicar partes del código o para escribir notas.
Es útil para proporcionar información adicional sobre el código.
También puedes usarlo para desactivar temporalmente partes del código durante la depuración.
"""

# Indentacion en Python

if 5 > 3:  
    print("5 es mayor que 3")
else:
    print("5 es menor que 3")

#Entrada de datos 

nombre_completo = input("Ingrese su nombre: ")
print(nombre_completo)

# Imprimir input y concatenación de variables

edad = int(input("Ingresa tu edad: "))
print("El nombre del usuario es " + nombre_completo + " y su edad es de " + str(edad) + " años ")
print(f"Mi nombre es {nombre_completo} y tengo {edad} años")

# Operadores aritméticos #

a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
potenciacion = a ** b
print("La suma es: " + str(suma))
print("La resta es: " + str(resta))
print("La multiplicacion es: " + str(multiplicacion))
print("La division es: " + str(division))
print("La potenciacion es: " + str(potenciacion))