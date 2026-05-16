#Operadores de asignacion
#Suma
x = 5 # Se le asignacion el valor
x +=2
print(x)
x = x + 5 #Suma y recicla la misma variable x
print(x)

#Resta
x = 20
x -= 20
print(x)

#Multiplicacion
x = 30
x *= 30
print(x)

#Divicion
x = x / 70
x /= 70
print(x)

#Modulo o asignacion
x = x % 3
x %= 3
print(x)

#Exponenciacion y asignacion
x = x ** 2
x **= 2
print(x)

#walrus operator (Python 3.8+)
print(x := 50)#Asigna 10 a x y luego imprime x
