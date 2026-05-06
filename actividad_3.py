#ACTIVIDAD 3 : CLASIFICADOR IMC
kg = float(input("ingrese su peso en kilogramos: "))
estatura_metros = float(input("ingrese su estatura en metros: "))

print("="*100)

imc = kg / (estatura_metros ** 2)

if imc < 18.5:
    print(f"Tu IMC es {round(imc,2)} estas bajito de peso")
elif imc >=18.5 and 25:
    print(f"Tu IMC es {round(imc,2)} Tu peso es normal")
elif imc >=25 and 30:
        print(f"Tu IMC es {round(imc,2)} Tu peso es de Sobrepeso")
elif imc >= 30:
        print(f"Tu IMC es {round(imc,2)} Tu peso es obsesidad")
        

    

