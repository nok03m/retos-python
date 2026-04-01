print("\n\t\t\tCalculadora nutricion rapida")

try:
    proteina = float(input("Ingrese los gramos de proteina: "))
    carbohidrato = float(input("Ingrese los gramos de carbohidrato: "))
    grasa = float(input("Ingrese los gramos de grasa: "))
except ValueError:
    print("\nERROR ---> Entrada invalida!!!")
else:
    total_calorias = (proteina * 4) + (carbohidrato * 4) + (grasa * 9)
    print(f"\nEl total de las calorias de la receta es: {total_calorias}")
finally:
    print("\nFinalizando programa...")
