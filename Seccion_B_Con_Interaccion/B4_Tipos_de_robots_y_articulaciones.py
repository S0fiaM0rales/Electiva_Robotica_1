# Selección del tipo de robot
print("1. Robot cilíndrico")
print("2. Robot cartesiano")
print("3. Robot esférico")

opcion = int(input("\nSeleccione el tipo de robot: "))


# Robot cilíndrico
if opcion == 1:

    tipo = "Cilíndrico"
    articulaciones = 3

    print("\nTipo de robot:", tipo)
    print("Número de articulaciones:", articulaciones)


# Robot cartesiano
elif opcion == 2:

    tipo = "Cartesiano"
    articulaciones = 3

    print("\nTipo de robot:", tipo)
    print("Número de articulaciones:", articulaciones)


# Robot esférico
elif opcion == 3:

    tipo = "Esférico"
    articulaciones = 3

    print("\nTipo de robot:", tipo)
    print("Número de articulaciones:", articulaciones)


else:

    print("\nOpción no válida.")