numero = int(input("Dime un número: "))

i = 2

while i < numero and numero % i != 0:
    i = i + 1

if numero > 1 and i == numero:
    print("Es primo")
else:
    print("No es primo")