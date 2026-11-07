numero = int(input("Ingrese un número: "))

for fila in range(1, numero + 1):

    linea = ""

    for columna in range(1, fila + 1):
        linea = linea + str(columna)

    print(linea)

        