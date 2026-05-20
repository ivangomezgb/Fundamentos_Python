from typing import Iterable


a,b,c = map(int, input("Ingrese").split())

print(a,b,c)


a = "hello"
b = a.strip("ho")
c = len(b)
print(c)


a = [1,2,3]
a.insert(1,5)
print(a)

a = 123
b = (a)
print(b+2)

x = 5
y = 10
if x > 3:
    if y > 8:
        if x + y >20:
            print("A")
        else:
            print("B")
    else:
        print("C")
else:
    print("D")
    
    print = "Hello world"
    print(print)
    
    
    import ramdom
    
    numero = ramdom
    intentos = 0
    while intentos < 5:
        if numero == 42:
            print("Hola")
            
            
# EJERCICIO 
numeros = [10,20,30,40,50]
resultado = numeros[::-1]
print(resultado)

# Ejerccio
tupla7 = tuple()
print(tupla7)

#Ejercicio 

crush = "Python"
print(crush * 2)

#Ejercicio
a = [1,2,3]
print(a * 2)


#Ejercicio
puntuacion = 10
if puntuacion > 5:
    print("Ganaste")