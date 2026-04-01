
def obtener_numero_mayor(lista_numeros):
    numero_mayor = 0
    
    for numero in lista_numeros:
        if numero > numero_mayor:
            numero_mayor = numero
    return numero_mayor

def obtener_numero_menor(lista_numeros):
    numero_menor = 999999999999
    
    for numero in lista_numeros:
        if numero < numero_menor:
            numero_menor = numero
    return numero_menor

def obtener_promedio(lista_numeros):
    suma = 0
    
    if not len(lista_numeros):
        return 0
    
    for numero in lista_numeros:
        suma += numero
        
    return suma / len(lista_numeros)

def obtener_pares_impares(lista_numeros):
    lista_pares = []
    lista_impares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
            
    return {
        "pares": lista_pares,
        "impares": lista_impares
    }
        
lista_numeros = []
print("\n\t\t\tEstadistica de una lista de numeros")

try:
    cantidad = int(input("\nIngresa la cantidad de numeros a recibir (cantidad > 0): "))
    
    if cantidad < 1:
        raise ValueError
    
    contador = 0
    while contador < cantidad:
        try:
            numero = int(input(f"Ingresa el {contador + 1} numero:   "))
            lista_numeros.append(numero)
            contador += 1
        except ValueError:
            print("ERROR ---> Entrada invalida!!!")
        
except ValueError:
    print("ERROR ---> Valor no permitido!!!")
else:
    numero_mayor = obtener_numero_mayor(lista_numeros)
    numero_menor = obtener_numero_menor(lista_numeros)
    promedio = obtener_promedio(lista_numeros)
    pares, impares = obtener_pares_impares(lista_numeros).values()

    print("\nEstadisticas de los valores ingresados")
    print(f"Número mayor: {numero_mayor} y Numero menor: {numero_menor}")
    print(f"Promedio: {promedio}")
    print(f"Cantidad pares: {len(pares)} y Cantidad impares: {len(impares)}\n")