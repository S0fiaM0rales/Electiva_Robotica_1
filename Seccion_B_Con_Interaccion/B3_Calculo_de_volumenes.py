import numpy as np

# Selección del sólido
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("\nSeleccione el sólido: "))


# PRISMA
if opcion == 1:

    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))

    # Cálculo del volumen
    volumen = area_base * altura

    print("\nVolumen del prisma:")
    print(volumen)


# PIRÁMIDE
elif opcion == 2:

    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))

    # Cálculo del volumen
    volumen = (area_base * altura) / 3

    print("\nVolumen de la pirámide:")
    print(volumen)


# CONO TRUNCADO
elif opcion == 3:

    radio_mayor = float(input("Ingrese el radio mayor: "))
    radio_menor = float(input("Ingrese el radio menor: "))
    altura = float(input("Ingrese la altura: "))

    # Cálculo del volumen
    volumen = (
        np.pi * altura / 3
        * (
            radio_mayor**2
            + radio_mayor * radio_menor
            + radio_menor**2
        )
    )

    print("\nVolumen del cono truncado:")
    print(volumen)


# CILINDRO
elif opcion == 4:

    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))

    # Cálculo del volumen
    volumen = np.pi * radio**2 * altura

    print("\nVolumen del cilindro:")
    print(volumen)


else:

    print("\nOpción no válida.")