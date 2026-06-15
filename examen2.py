comentario = input("Ingresa tu comentario: ")

if "malo" in comentario.lower():
    print("Alerta: Se ha detectado la palabra 'malo' en tu comentario.")
else:
    print("Comentario aceptado.")
