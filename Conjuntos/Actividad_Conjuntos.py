python_curso ={'Ana','Luis','Marta','Carlos','Sofia','Pedro'} 
java_curso = {'Luis','Carlos','Pedro','Laura','Diego'}
bd_curso = {'Marta','Sofia','Laura','Ana','Miguel'}

#Total de aprendices unicos en los tres cursos
total_aprendices = python_curso.union(java_curso).union(bd_curso)
print(f"El total de aprendices unicos en los tres cursos es de {len(total_aprendices)}")

print("="*100)
#Total de aprendices que solo cursan python y java pero no bd
python_curso, java_curso, bd_curso = python_curso, java_curso, bd_curso
solo_python_java = (python_curso.intersection(java_curso)).difference(bd_curso)
print(f"El total de aprendices que solo cursan python y java pero no bd son {len(solo_python_java)}")

print("="*100)

#Los aprendices que cursan python pero no java ni bd
solo_python = python_curso.difference(java_curso).difference(bd_curso)
print(f"Los aprendices que cursan solo python pero no java ni bd son {len(solo_python)}")

print("="*100)

#Los aprendices que estan exactamente en dos cursos 
exactamente_dos_cursos = (python_curso.intersection(java_curso)).difference(bd_curso).union((python_curso.intersection(bd_curso))).union((java_curso.intersection(bd_curso)))
print(f"Los aprendices que estan exactamente en dos cursos son {len(exactamente_dos_cursos)}")

print("="*100)


# Lista de inscripciones con duplicados
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']

# Los conjuntos (set) eliminan automáticamente los duplicados
aprendices_unicos = set(inscripciones)

print(f"Cantidad de aprendices únicos inscritos: {len(aprendices_unicos)}")
print(f"Los aprendices unicos son {aprendices_unicos}")
print("="*100)


# aprendices inscritos en 3 programas diferente:
programa_SST = {'Ana', 'Luis', 'Marta', 'Carlos'}
programa_ADSO = {'Ana', 'Sofia', 'Luis'}
programa_TOPOGRAFIA = {'Ana', 'Pedro', 'Luis', 'Carlos'}

# La UNIÓN de todos los programas nos da el total de aprendices únicos en la institución
todos_los_aprendices = programa_SST.union(programa_ADSO, programa_TOPOGRAFIA)


# 4. Comprensión de diccionario para contar en cuántos programas está cada uno
conteo_programas = {
    aprendiz: (
        (1 if aprendiz in programa_SST else 0) +
        (1 if aprendiz in programa_ADSO else 0) +
        (1 if aprendiz in programa_TOPOGRAFIA else 0)
    )
    for aprendiz in todos_los_aprendices
}

print("Conteo de programas por aprendiz:")
print(conteo_programas)
print("="*100)


# BONUS: Identificar quién está en los tres programas a la vez
# Usamos la INTERSECCIÓN (&) que encuentra solo los elementos que se repiten en TODOS los conjuntos
en_los_tres = programa_SST.intersection(programa_ADSO, programa_TOPOGRAFIA)

print(f"Aprendices matriculados en los tres programas a la vez: {en_los_tres}")  # {'Ana', 'Luis'} 