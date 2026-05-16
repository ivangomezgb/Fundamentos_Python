# Calculadora simple en Python
# Ingresar dos números y seleccionar la operación a realizar

num_1= int(input("Ingrese el primer numero: "))
num_2= int(input("Ingrese el segundo numero: "))
tipo_operacion = input("Ingrese la operación que desea realizar (1 suma, 2 resta, 3 multiplicacion, 4 division, 5 potenciacion): ")
# Realizar la operación seleccionada por el usuario #
suma=num_1+num_2
resta=num_1-num_2  
multiplicacion=num_1*num_2
division=num_1/num_2
potenciacion=num_1**num_2
# Imprimir el resultado de la operación seleccionada por el usuario #
# El resultado se muestra dependiendo de la operación seleccionada por el usuario #
if tipo_operacion == "1":
    print("El resultado de la suma es: " + str(suma))
elif tipo_operacion == "2":
    print("El resultado de la resta es: " + str(resta))
elif tipo_operacion == "3":
    print("El resultado de la multiplicacion es: " + str(multiplicacion))
elif tipo_operacion == "4":
    print("El resultado de la division es: " + str(division))
elif tipo_operacion == "5":
    print("El resultado de la potenciacion es: " + str(potenciacion)) 