frase = input("Escribe una frase: ").lower()

if "triste" in frase:
    frase_modificada = frase.replace("triste", "feliz")
    print("Frase editada:", frase_modificada)
else:
    print("Frase en mayúsculas:", frase.upper())
