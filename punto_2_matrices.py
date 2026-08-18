import numpy as np

# Matrices previamente inicializadas
matriz_A = np.array([
    [1, 2],
    [3, 4]
])

matriz_B = np.array([
    [5, 6],
    [7, 8]
])

# Suma
suma = matriz_A + matriz_B

# Resta
resta = matriz_A - matriz_B

# Multiplicación elemento a elemento
producto_elemento = matriz_A * matriz_B

# Producto matricial
producto_matricial = np.dot(matriz_A, matriz_B)

# División elemento a elemento
division = matriz_A / matriz_B

# RESULTADOS
print("MATRIZ A:")
print(matriz_A)

print("\nMATRIZ B:")
print(matriz_B)

print("\nSuma:")
print(suma)

print("\nResta:")
print(resta)

print("\nMultiplicación elemento a elemento:")
print(producto_elemento)

print("\nProducto matricial:")
print(producto_matricial)

print("\nDivisión elemento a elemento:")
print(division)
