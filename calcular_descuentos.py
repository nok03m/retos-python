
def limpiar_consola():
    print("\033[H\033[2J", end="")

quiere_salir = ""

while quiere_salir != "S":
    descuento = 0
    total = 0
    
    print("\n\t\tCalculadora de descuentos")
    precio = int(input("Ingresa el precio del producto: $"))
    
    print("\nDescuentos disponibles:")
    print("Alimentos → 5%\nRopa → 10%\nElectronica → 15%\nHogar → 8%\n")
    
    while True:
        categoria = input("Ingresa la categoria: ").capitalize()

        if categoria == "Alimentos":
            descuento = 5
        elif categoria == "Ropa":
            descuento = 10
        elif categoria == "Electronica":
            descuento = 15
        elif categoria == "Hogar":
            descuento = 8
        else:
            print("ERROR ---> No ingresaste una categoria valida!!\n")
            continue
        break
    total = precio - ((precio * descuento) / 100)
    
    print(f"\nAplicaste a un descuento de {descuento}%\nTotal a pagar: ${total}")

    while True:
        quiere_salir = input("\nFinalizar el programa? S/N   ").capitalize()
        if quiere_salir == "S":
            limpiar_consola()
            print("Cerrando programa... Hasta la proxima!!!\n")
            break
        elif quiere_salir == "N":
            limpiar_consola()
            break
        else:
            print("ERROR ---> Solo se permite S/N!!!")
