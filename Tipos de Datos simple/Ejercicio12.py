barras = int(input("Cuantas barras: "))

precio = 3.49
descuento = precio * 0.60
final = barras * (precio - descuento)

print("Precio normal:", precio)
print("Descuento:", descuento)
print("Precio final:", final)