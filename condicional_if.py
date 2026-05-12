#CONDICIONAL IF / ELSE / ELIF

if False:
    print("La primera condicion es verdadera")
elif False:
    print("La segunda condicion es verdadera elif")
elif True:
    print("La tercera condicion es verdadera elif")
else:
    print("La condicion es falsa")

#Ejercicio: Clasificacion de edad 

edad = int(input("Ingresa tu edad "))

if edad < 18:
    print(f"Tienes {edad} años eres menor de edad")
elif edad >= 18 and edad < 65:
    print(f"Tienes {edad} años eres adulto")
else :
    print(f"Tienes {edad} años eres adulto mayor")

    
#Ejercicio : Clasificacion de Edad IF anidado

edad = int(input("Ingresa tu edad "))

if edad < 18:
    if edad > 12 and edad < 18:
        print("Adolescente")
    else:
        print("Niño")
else:
    if edad >=18 and edad < 60:
        print(f"Tienes {edad} años eres adulto")
    else:
        print(f"Tienes {edad} años eres adulto mayor")
    
#Operador ternario

numero = int(input("Ingresa un numero "))

if numero % 2 == 0:
    print(f"El numero es {numero} y es par ")
else:
    print(f"El numero es {numero} y es impar ")
