
print("\n\t\t\tCalculadora de Indice de Masa Corporal (IMC)")
imc = 0

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    if peso <= 0 or altura <= 0:
        raise ValueError
except ValueError:
    print("\nERROR ---> Entrada invalida!!!")
else:
    imc = peso / (altura * altura)
    print(f"\nSu indice de Masa Corporal (IMC) es: {imc}")
finally:
    print("\nFinalizando programa...")