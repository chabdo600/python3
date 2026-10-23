
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M/F): ")

if (sexo.upper() == "F" and nombre.upper() < "M") or (sexo.upper() == "M" and nombre.upper() > "N"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

