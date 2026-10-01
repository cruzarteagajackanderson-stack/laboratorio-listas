
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


# ==========================================================
# ETAPA 2: MATRIZ BIDIMENSIONAL 3x3
# ==========================================================

def etapa_2():
    print("\n" + "=" * 55)
    print("ETAPA 2: MATRIZ BIDIMENSIONAL 3x3")
    print("=" * 55)

    matriz = []

    print("\nIngrese 9 números para llenar la matriz:")

    # Crear y llenar una matriz de 3 filas por 3 columnas
    for fila in range(3):
        nueva_fila = []

        for columna in range(3):
            valor = leer_entero(
                f"Ingrese el valor para la posición [{fila}][{columna}]: "
            )
            nueva_fila.append(valor)

        matriz.append(nueva_fila)

    # Mostrar la matriz en formato de filas y columnas
    print("\nMatriz ingresada:")

    for fila in range(3):
        for columna in range(3):
            print(f"{matriz[fila][columna]:5}", end="")
        print()

    # Calcular la suma de todos los elementos
    suma_total = 0

    for fila in range(3):
        for columna in range(3):
            suma_total += matriz[fila][columna]

    print(f"\nLa suma total de la matriz es: {suma_total}")


# PROGRAMA PRINCIPAL

etapa_1()
etapa_2()