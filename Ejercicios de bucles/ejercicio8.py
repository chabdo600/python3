altura = int(input("Dime la altura: "))

fila = 1

while fila <= altura:
    numero = fila * 2 - 1

    while numero >= 1:
        print(numero, end=" ")
        numero = numero - 2

    print()
    fila = fila + 1