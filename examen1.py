
while True:
    texto = input("Escribe algo (escribe 'fin' para salir): ").strip().lower()
    if texto == "fin":
        print("Sesión finalizada.")
        break
    else:
        print(f"Texto ingresado: {texto}")
