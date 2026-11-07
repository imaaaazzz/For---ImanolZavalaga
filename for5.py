suma = 0
contar = 0 
print("Ingrese 10 números, si desea salir ingrese 0")

for i in range(10):
    numero = int(input("Ingrese un número: "))

    if numero == 0:
        break
    else:
        suma += numero
        contar += 1
  
    print(numero)

if contar > 0:
    promedio = suma / (contar)
    print(f"El promedio de los números ingresados es: {promedio}")
    
    print(f"La suma de los números ingresados es: {suma}")
else:
    print("No se ingresaron números para calcular el promedio y la suma.")