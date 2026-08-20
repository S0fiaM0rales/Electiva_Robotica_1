# Pregunta inicial
respuesta = input("¿Desea continuar? Si/No: ")

# Convertir respuesta a minúsculas
respuesta = respuesta.lower()


# Repetir hasta que el usuario escriba No
while respuesta != "no":

    print("\nEl programa continúa.")

    respuesta = input("¿Desea continuar? Si/No: ")
    respuesta = respuesta.lower()


print("\nPrograma finalizado.")