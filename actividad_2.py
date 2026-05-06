#ACTIVIDAD 2 : Calculadora de notas 


def leer_nota(numero):
    nota = float(input(f"Ingresa la calificacion {numero} del parcial: "))
    while nota < 1 or nota > 5:
        print("La nota debe estar entre 1 y 5. INTENTE NUEVAMENTE")
        nota = float(input(f"Ingresa la calificacion {numero} del parcial: "))
    print("=" * 100)
    return nota

califi_parcial1 = leer_nota(1)
califi_parcial2 = leer_nota(2)
califi_parcial3 = leer_nota(3)

print("=" * 100)

#PROMEDIO NOTAS
promedio = (califi_parcial1 + califi_parcial2 + califi_parcial3) / 3


if promedio >= 3:
    print("      🟩APROBADO")
else:
    puntos_faltantes = 3 - promedio
    print(f"El promedio es {round(promedio,1)}")
    print("="*100)
    print(f"Te falta {round(puntos_faltantes,1)} puntos para aprobar")
    print("="*100)
    print("         ✖️ REPROBADO")


