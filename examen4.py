
password = ""
while password.strip() == "":
    password = input("Ingrese su contraseña: ").strip()

if password == "secreto123": # Cambiar por la contraseña deseada
    print("Acceso concedido.")
else:
    print("Acceso denegado. Contraseña incorrecta.")
