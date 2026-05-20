# Estructura diccionarios

diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

# Diccionario vacio

diccionario_vacio = {}

# Diccionario con elementos 

diccionario_aprendiz = {
    "nombre": "Leo",
    "edad": 25,
    "programa": "ADSO",
    "semestre": 4
}

print(type(diccionario_aprendiz))

#Obtener un valor del diccionario
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz.get("programa"))

#Obtener solo llaves del diccionario 
print(diccionario_aprendiz.keys())

# Obtener los valores del diccionario
print(diccionario_aprendiz.values())

# Obtener la clave y el valor del diccionario 
print(diccionario_aprendiz.items())

#Agregar nuevo elemento al diccionario 
diccionario_aprendiz["correo"]= "ivanleon@gmail.com"

#Modificar un valor del diccionario

diccionario_aprendiz["programa"] = "ADSO"
print(diccionario_aprendiz)

# Metodo update()
diccionario_aprendiz.update({"nombre":"Leito"}) #modifica un elemento
diccionario_aprendiz.update({"edad":"18"}) #agrega un elemento
print(diccionario_aprendiz)

#Comprobar pertenencia (in)

if "programa" in diccionario_aprendiz:
    print("Programa es una de las propiedades de este diccionario")
    
    
# Recorrer solo las llaves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)
    
# Recorrer sololos valores del diccionario
for valor in diccionario_aprendiz.values():
    print(valor)
    
# Recorrer las claves y los valores del diccionario 
for clave_valor in diccionario_aprendiz.items():
    print(f" las claves y el valor son {clave_valor}")
    
#Eliminar elementos en el diccionario POP()
diccionario_aprendiz.popitem() #Elimina el ultimo elemento agregado
print(diccionario_aprendiz)

# Eliminar edad o clave y valor especificamente
diccionario_aprendiz.pop("edad") # Elimina un elemento especifico
print(diccionario_aprendiz)

diccionario_aprendiz.clear() #Elimina todos los elementos del diccionario
print(diccionario_aprendiz)


#DICCIONARIOS ANIDADOS

aprendices = {
    "aprendiz_1": {
        "nombre": "Julian",
        "edad": 22,
        "programa": "SST"
    },
    "aprendiz_2": {
        "aprendiz_2": {
            "nombre": "DANIEL",
            "edad": 23,
            "programa": "TOPOGRAFIA"
        }
    },
    "aprendiz_3": {
        "aprendiz_3": {
            "nombre": "Leo",
            "edad": 25,
            "programa": "ADSO"
        }
    }
}

#Acceder a un valor especifico en un diccionario anidado
print(aprendices["aprendiz_3"]["aprendiz_3"]["nombre"])

# Recorrer un diccionario anidado con el ciclo for

for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}")
    for clave,valor in datos.items():
        print(f" {clave} : {valor}")
        
        
