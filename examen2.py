comentario = input("Ingresa tu comentario: ").lower()

if "malo" in comentario:
    print("Alerta: Se ha detectado la palabra 'malo' en tu comentario.")
else:
    print("Comentario aceptado.")
