
# LABORATORIO: LISTAS, MATRICES Y ORDENAMIENTOS
# Estudiante: Anderson Cruz


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingresa un número entero.")



# ETAPA 1: LISTA UNIDIMENSIONAL


def etapa_1():
    print("\n" + "=" * 55)
    print("ETAPA 1: LISTA UNIDIMENSIONAL")
    print("=" * 55)

    # Lista de 10 números enteros
    numeros = [15, 8, 27, 40, 12, 35, 6, 19, 50, 22]

    # Recorrido e impresión usando for
    print("\nLista inicial:")
    for i in range(len(numeros)):
        print(f"Posición {i}: {numeros[i]}")

    # Modificar el tercer elemento
    nuevo_valor = leer_entero("\nIngrese un nuevo valor para el tercer elemento: ")
    numeros[2] = nuevo_valor

    print("\nLista después de modificar el tercer elemento:")
    for i in range(len(numeros)):
        print(f"Posición {i}: {numeros[i]}")

    # Buscar un valor
    valor_buscar = leer_entero("\nIngrese el número que desea buscar: ")

    if valor_buscar in numeros:
        posicion = numeros.index(valor_buscar)
        print(f"El número {valor_buscar} existe en la lista.")
        print(f"Se encuentra en la posición {posicion}.")
    else:
        print(f"El número {valor_buscar} no existe en la lista.")



# PROGRAMA PRINCIPAL


etapa_1()