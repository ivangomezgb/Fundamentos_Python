# CONJUNTOS (SETS) EN PYTHON

#ESTRUCTURA DE UN CONJUNTO

conjunto = set()

print(type(conjunto)) # class set esto si es un set

#----CREATE THE CONJUNTOS----

lenguajes = {"Python","Java","C++","Python","Java"}

print(lenguajes)

#Metodos de mofificacion ----

frutas = {"mango","guayaba","mora"}
frutas.add("naranja") # agrega un elemento y si agrega el mismo nombre no lo agrega por duplicidad
frutas.remove("mango") # elimina un elemento lanza un Keyerror si no existe
frutas.discard("mora") # elimina; no lanza error si no existe
element = frutas.pop() # elimina y retorna un elemento aleatorio
print(element)

#------- Verificar pertenencia ----
print("Python" in lenguajes) # TRUE -INSTANTANEO SIN IMPORTAR TAMAÑO

print("COBOL" in lenguajes) # FALSE



python_devs = {"Ana","Luis","Martha","Carlos","Sofia"}
java_devs = {"Luis","Carlos","Pedro","Laura"}


# UNION  |  : todos los elementos de ambos conjuntos

todos =   python_devs | java_devs 
# o tambien: union = python_devs.union(java_devs)
print("Union", todos)

# {"Ana","Luis","Martha","Carlos","Sofia","Pedro" , "Laura"}



#Interseccion & : solo los que estan en ambos

ambos = python_devs & java_devs
# o tambien: interseccion = python_devs.intersection(java_devs)
print("Interseccion" , ambos) # {'Luis','Carlos'}


#DIFERENCIA  -  : los de A que NO estan en B

solo_python = python_devs - java_devs
# o tambien diference = python_devs.diference(java_devs)
print("Solo python", solo_python) # {'Ana','Martha','Sofia'}

solo_java = java_devs - python_devs
print("Solo java", solo_java) # {'Pedro','Laura'}


#DIFERENCIA SIMETRICA  ^  : LOS QUE ESTAN EN 1 PERO NO EN AMBOS

exclusivos = python_devs ^ java_devs
# o tambien: solo1_lenguaje = python_devs.symmetric_difference(java_devs)

print("Exclusivos", exclusivos) # {'Ana','Martha','Sofia','Pedro','Laura'}
