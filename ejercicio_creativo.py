#Ejercicio practico INPUT,ELSE,IF,ELIF,CONDICIONALES,PRINT 
#---------------------------------------------------------------------------------------------------------------
bateria= int(input("Ingresa el porcentaje 'eje 45' "))
while bateria <0 or bateria >100:
    print("Elija un rango de 0 a 100% . ⚠️ INTENTE NUEVAMENTE")
    kg = float(input("Ingresa el porcentaje 'eje 45' : "))

if bateria == 100:
    print("Carga Completa")
    print("   ______________________________________")
    print(f"  | 10:24   📶 VoLTE WiFi      🔋{bateria}%    |")
    print("  |--------------------------------------|")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |______________________________________|")
elif bateria >= 20:
    print("Esta normal")
    print("   ______________________________________")
    print(f"  | 10:24   📶 VoLTE WiFi      🔋{bateria}%     |")
    print("  |--------------------------------------|")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |______________________________________|")

elif bateria < 20 and bateria >= 5:
    print("Se recomienda cargar el dispositivo")
    print("   ______________________________________")
    print(f"  | 10:24   📶 VoLTE WiFi      🔋{bateria}%     |")
    print("  |--------------------------------------|")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |                                      |")
    print("  |______________________________________|")
elif bateria <= 5 and bateria > 0:
    print("Ahorro de energia activado")
    print("   ______________________________________")
    print(f"  | 10:24   📶 VoLTE WiFi     🔋{bateria}%⚡     |")
    print("  |--------------------------------------|")
    print("  |                                      |")
    print("  |     AHORRO DE BATERÍA ACTIVADO       |")
    print("  |   ↓ rendimiento / ↓ consumo          |")
    print("  |                                      |")
    print("  |______________________________________|")
else:
    print("   ______________________________________")
    print(f"  |🔋{bateria}%⚡  ...Apagando el dispositivo    |")
    print("  |______________________________________|")
    print("  |                                      |")
    print("  |             Apagando...              |")
    print("  |            ●   ●   ●                 |")
    print("  |                                      |")
    print("  |______________________________________|")
    
print("GRACIAS POR PROBAR MI CREATIVIDAD")