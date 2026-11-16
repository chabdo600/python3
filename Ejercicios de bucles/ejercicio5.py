capital = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual: "))
años = int(input("Número de años: "))

for i in range(años):
    capital = capital + capital * interes / 100
    print(capital)