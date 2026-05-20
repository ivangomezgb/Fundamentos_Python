
#Sistema de registro de aprendices 


Diccionario_grupo = {
    "Aprendiz_1": {
        "nombre": "Julian Univio",
        "edad": 22,
        "notas": [2.5, 3.8, 2.0, 2.0],
        "ciudad": "Bogotá"
    },
    "Aprendiz_2": {
        "nombre": "Ivan Gomez",
        "edad": 19,
        "notas": [3.2, 4.1, 3.5, 3.9],
        "ciudad": "Medellín"
    },
    "Aprendiz_3": {
        "nombre": "Sthepany Suelto",
        "edad": 25,
        "notas": [5.0, 4.8, 4.9, 4.7],
        "ciudad": "Cali"
    },
    "Aprendiz_4": {
        "nombre": "Miguel Castañeda",
        "edad": 21,
        "notas": [2.8, 1.5, 1.0, 3.1],
        "ciudad": "Bucaramanga"
    }
}

#Formula calcular_promedio que reciba la lista de notas y retorne el promedio.
nota_1 = Diccionario_grupo["Aprendiz_1"]["notas"]
nota_2 = Diccionario_grupo["Aprendiz_2"]["notas"]
nota_3 = Diccionario_grupo["Aprendiz_3"]["notas"]
nota_4 = Diccionario_grupo["Aprendiz_4"]["notas"]

todas_las_notas = [nota_1, nota_2, nota_3, nota_4]

promedio_general = sum(nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"El promedio general de las notas de los aprendices es de {promedio_general}")

print("="*100)
# calcula el promedio con items y un ciclo for e imprime un resultado con ficha, nombre y promedio de notas y estado de aprobado o reprobado
# dependiendo del promedio de notas siendo aprobado si el promedio es mayor o igual a 3.0 y reprobado si el promedio es menor a 3.0


calcular_promedio = Diccionario_grupo.items()
for aprendiz, datos in calcular_promedio:
    nombre = datos["nombre"]
    edad = datos["edad"]
    notas = datos["notas"]
    promedio = sum(notas) / len(notas)
    estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
    print(f"El aprendiz {nombre} de {edad} años tiene un promedio de {promedio} y el estado es {estado}")

print("="*100)

# Agrega un nuevo aprendiz al diccionario después de crearlo, usando una nueva
#clave de ficha. Luego actualiza la ciudad de uno de los aprendices existentes con
# dicc[ficha]['ciudad'] = 'Nueva Ciudad'

Diccionario_grupo["Aprendiz_5"] = {
    "nombre" : "Juan Castañeda",
    "edad" : 18,
    "notas" : [2.0, 3.0, 4.0, 5.0],
    "ciudad" : "Yopal"
}


Diccionario_grupo["Aprendiz_5"]["ciudad"] = "Villavicencio"

print(Diccionario_grupo["Aprendiz_5"])


print("="*100)

#Bonus: Usa sorted() con key= para imprimir la lista de aprendices ordenada de mayor a menor promedio.
aprendices_ordenados = sorted(
    Diccionario_grupo.items(), 
    key=lambda x: sum(x[1]["notas"]) / len(x[1]["notas"]), 
    reverse=True
)

print("Ranking de Aprendices (Mayor a Menor Promedio):")
for ficha, datos in aprendices_ordenados:
    promedio = sum(datos["notas"]) / len(datos["notas"])
    print(f"El aprendiz {datos['nombre']} tiene un Promedio de {round(promedio, 2)}")