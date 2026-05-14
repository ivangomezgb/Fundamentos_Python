

from operator import pos


lista_canciones = ["Choque","Pal agua","Gasolina","Dile","Candy"]
lista_nueva = ["BonusTrack 1", "Bonus Track 2"]

# Metodos en orden y estado de las listas despues de cada metodo

print("=" *55)

cancion_final = lista_canciones.append("Dura")
print(f"Lista de canciones despues de agregar al final Dura es : {lista_canciones}")


print("=" *55)

cancion_posicion = lista_canciones.insert(2,"Despacito")
print(f"Lista de canciones al agregar Despacito en la posicion 2 {lista_canciones}")

print("=" *55)

fusion_lista = lista_canciones.extend(lista_nueva)
print(f"La lista de canciones al fusionar con la lista nueva asi quedo {lista_canciones}")

# Metodo de eliminar 
print("=" *55)

delete_name = lista_canciones.remove("Gasolina")
print(f"La lista al eliminar la cancion Gasolina queda asi {lista_canciones}")

print("=" *55)

delete_posicion = lista_canciones.pop(7)
print(f"La lista al eliminar la cancion en el indice 7 queda asi {lista_canciones}")

#Sort para ordenar toda la lista alfabeticamente

print("=" *55)

lista_alfa = lista_canciones.sort()
print(f"La lista esta ordenada alfabeticamente y quedo asi {lista_canciones}")

print("=" *55)

#Preguntas

#Cuantas canciones tiene la playlist

num_canciones = len(lista_canciones)
print(f"La playlist tiene un total de {num_canciones} canciones")

print("=" *55)

#En que posicion se encuentra la primera cancion que agregue

position_cancion = lista_canciones.index("Dura")
print(f"La cancion se encuentra en la posicion {position_cancion} de la lista")

print("=" *55)

#Cuantas veces aparece el string 'Bonus Track 1'

veces_bonus = lista_canciones.count("Bonus Track 1")
print(f"El string 'Bonus Track 1' aparece {veces_bonus} veces en la lista")