import numpy as np
import matplotlib.pyplot as plt

# Coordenadas ingresadas por teclado
x = float(input("Ingrese la coordenada X: "))
y = float(input("Ingrese la coordenada Y: "))
z = float(input("Ingrese la coordenada Z: "))

# Crear figura
fig = plt.figure()

# Crear sistema coordenado 3D
ax = fig.add_subplot(111, projection="3d")

# Dibujar vector
ax.quiver(
    0, 0, 0,
    x, y, z
)

# Dibujar punto final
ax.scatter(x, y, z)

# RESULTADOS
print("\nCoordenadas del vector:")
print("X:", x)
print("Y:", y)
print("Z:", z)


# Nombres de los ejes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.title("Vector en sistema coordenado 3D")

plt.show()