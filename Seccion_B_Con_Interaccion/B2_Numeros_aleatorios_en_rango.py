import numpy as np

# Datos ingresados por teclado
cantidad = int(input("Ingrese la cantidad de números aleatorios: "))
limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

# Generación de números aleatorios
numeros = np.random.randint(
    limite_inferior,
    limite_superior + 1,
    cantidad
)

# RESULTADOS
print("\nCantidad de números:", cantidad)
print("Rango:", limite_inferior, "a", limite_superior)

print("\nNúmeros aleatorios:")
print(numeros)