#ACTIVIDAD 2 : Calculadora de notas 

califi_parcial1 = float(input("Ingresa la calificacion 1 del parcial: "))
while califi_parcial1 <=0 or califi_parcial1 >=5:
    print("La nota debe estar entre 1 y 5 . INTENTE NUEVAMENTE")
    califi_parcial1 = float(input("Ingresa la calificacion 1 del parcial: "))
print("=" * 100)
califi_parcial2 = float(input("Ingresa la calificacion 2 del parcial: "))
print("=" * 100)
califi_parcial3 = float(input("Ingresa la calificacion 3 del parcial: "))

#===========================================================================


print("=" * 100)

#PROMEDIO NOTAS
promedio = (califi_parcial1 + califi_parcial2 + califi_parcial3) / 3


if promedio >= 3:
    print("      APROBADO")
else:
    puntos_faltantes= 3 - promedio
    print(f"El promedio es {round(promedio,1)}")
    print("="*100)
    print(f"Te falta {round(puntos_faltantes,1)} puntos para aprobar")
    print("="*100)
    print("         REPROBADO")


