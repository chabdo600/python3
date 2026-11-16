contrasena_correcta = "secreta123"
contrasena_usuario = input("Introduce la contraseña: ")

while contrasena_usuario != contrasena_correcta:
    print("Contraseña incorrecta")
    contrasena_usuario = input("Introduce la contraseña: ")

print("Contraseña correcta")