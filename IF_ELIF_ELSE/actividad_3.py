#ACTIVIDAD 3 : CLASIFICADOR IMC
kg = float(input("ingrese su peso en kilogramos: "))
while kg <=0 or kg >=100000000:
    print("Los valores deben ser ➕ positivos . ⚠️ INTENTE NUEVAMENTE")
    kg = float(input("ingrese su peso en kilogramos: "))
estatura_metros = float(input("ingrese su estatura en metros: "))
while estatura_metros <=0 or estatura_metros >=100000000:
    print("Los valores deben ser ➕ positivos . ⚠️ INTENTE NUEVAMENTE")
    kg = float(input("ingrese su estatura en metros : "))
print("="*100)

imc = kg / (estatura_metros ** 2)

if imc < 18.5:
    print(f"Tu IMC es {round(imc,2)} Clasificacion: Bajito de peso")
elif imc >=18.5 and imc <=25:
    print(f"Tu IMC es {round(imc,2)} Clasificacion: Normal")
elif imc >=25 and imc <=30:
        print(f"Tu IMC es {round(imc,2)} Clasificacion: Sobrepeso")
elif imc >= 30:
        print(f"Tu IMC es {round(imc,2)} Clasificacion: Obsesidad")
        

    

