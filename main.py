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


# ETAPA 2: MATRIZ BIDIMENSIONAL 3x3


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


# ETAPA 3: ORDENAMIENTO BURBUJA


def etapa_3():
    print("\n" + "=" * 55)
    print("ETAPA 3: ORDENAMIENTO BURBUJA")
    print("=" * 55)

    # Lista de números desordenados
    numeros = [34, 12, 45, 7, 23, 56, 18, 3, 41, 29]

    print("\nLista original:")
    print(numeros)

    # Ordenamiento burbuja, de menor a mayor
    for i in range(len(numeros) - 1):
        for j in range(len(numeros) - 1 - i):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    print("\nLista ordenada de menor a mayor:")
    print(numeros)


# ETAPA 4: ORDENAMIENTO POR SELECCIÓN


def etapa_4():
    print("\n" + "=" * 55)
    print("ETAPA 4: ORDENAMIENTO POR SELECCIÓN")
    print("=" * 55)

    # Lista distinta de la usada en el ordenamiento burbuja
    numeros = [64, 25, 12, 22, 11, 90, 5, 38, 17, 42]

    print("\nLista original:")
    print(numeros)

    # Busca el menor elemento y lo coloca al inicio
    for i in range(len(numeros) - 1):
        posicion_menor = i

        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[posicion_menor]:
                posicion_menor = j

        numeros[i], numeros[posicion_menor] = (
            numeros[posicion_menor],
            numeros[i]
        )

    print("\nLista ordenada de menor a mayor:")
    print(numeros)

# PROGRAMA PRINCIPAL


etapa_1()
etapa_2()
etapa_3()
etapa_4()