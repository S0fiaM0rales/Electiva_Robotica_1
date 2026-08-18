import numpy as np
import math


def rotacion_x(angulo):
    """
    Calcula la matriz de rotación alrededor del eje X.
    El ángulo se ingresa en grados.
    """

    theta = math.radians(angulo)

    matriz = np.array([
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)]
    ])

    return matriz


def rotacion_y(angulo):
    """
    Calcula la matriz de rotación alrededor del eje Y.
    El ángulo se ingresa en grados.
    """

    theta = math.radians(angulo)

    matriz = np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ])

    return matriz


def rotacion_z(angulo):
    """
    Calcula la matriz de rotación alrededor del eje Z.
    El ángulo se ingresa en grados.
    """

    theta = math.radians(angulo)

    matriz = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])

    return matriz


# Ángulo previamente inicializado
angulo = 30

# Calcular matrices de rotación
Rx = rotacion_x(angulo)
Ry = rotacion_y(angulo)
Rz = rotacion_z(angulo)

# Mostrar resultados
print(f"Ángulo de rotación: {angulo}°")

print("\nMatriz de rotación en X:")
print(np.round(Rx, 4))

print("\nMatriz de rotación en Y:")
print(np.round(Ry, 4))

print("\nMatriz de rotación en Z:")
print(np.round(Rz, 4))
