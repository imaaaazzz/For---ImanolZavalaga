
numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    
    contador = 0

    for j in range(1, i + 1):
        if i % j == 0:
            contador += 1

    if contador == 2:
        print(f"{i} es primo")
    else:
        print(f"{i} no es primo")