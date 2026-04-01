def limpiar_consola():
    print("\033[H\033[2J", end="")

reintentar = ""

while reintentar != "N":
    try:
        print("\n\t\t\tVerificar si un numero es primo")
        numero = int(input("Ingresa un numero: "))
        divisores = []

        if numero < 0:
            limpiar_consola()
            print("ERROR ---> El numero no puede ser negativo")
            continue
        elif numero == 0:
            pass
        elif numero > 0:    
            for index in range(1, numero + 1):
                if numero % index == 0:
                    divisores.append(index)
        
        if len(divisores) == 2:
            print(f"\nEl numero {numero} SI es primo")
        else:
            print(f"\nEl numero {numero} NO es primo")
            print(f"Divisores: {divisores}")
                 
    except ValueError:
        limpiar_consola()
        print("ERROR ---> El valor de entrada es invalido")
        continue
        
    while True:
        reintentar = input("\nQuieres probar con otro numero? S/N   ").capitalize()
        
        if reintentar == "S" or reintentar == "N":
            limpiar_consola()
            break
        else:
            limpiar_consola()
            print("ERROR ---> Solo se permite S/N!!!")