
password = "12345"
while password.strip() == "12345":
    password = input("Ingrese su contraseña: ").strip()
if password == "12345": # Cambiar por la contraseña deseada
    print("Acceso denegado. Contraseña incorrecta")
else:
    print("Acceso Concedido")
