import numpy as np

vector_A = np.array([2, 4, 6])
vector_B = np.array([1, 3, 5])

# Suma
suma = vector_A + vector_B

# Resta
resta = vector_A - vector_B

# Producto elemento a elemento
producto = vector_A * vector_B

# Producto punto
producto_punto = np.dot(vector_A, vector_B)

# Producto cruz
producto_cruz = np.cross(vector_A, vector_B)

# División elemento a elemento
division = vector_A / vector_B

# RESULTADOS
print("VECTOR A:", vector_A)
print("VECTOR B:", vector_B)

print("\nSuma:")
print(suma)

print("\nResta:")
print(resta)

print("\nProducto elemento a elemento:")
print(producto)

print("\nProducto punto:")
print(producto_punto)

print("\nProducto cruz:")
print(producto_cruz)

print("\nDivisión elemento a elemento:")
print(division)
