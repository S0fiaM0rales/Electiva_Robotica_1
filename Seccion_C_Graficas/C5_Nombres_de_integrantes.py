import numpy as np
import matplotlib.pyplot as plt


# Función para dibujar una letra
def dibujar_letra(letra, x, y, escala=1):

    if letra == "A":
        plt.plot(
            [x, x + 0.5 * escala, x + 1 * escala],
            [y, y + 1 * escala, y]
        )

        plt.plot(
            [x + 0.25 * escala, x + 0.75 * escala],
            [y + 0.5 * escala, y + 0.5 * escala]
        )

    elif letra == "D":
        plt.plot(
            [x, x, x + 0.6 * escala],
            [y, y + 1 * escala, y + 1 * escala]
        )

        theta = np.linspace(np.pi / 2, -np.pi / 2, 50)

        plt.plot(
            x + 0.6 * escala + 0.4 * escala * np.cos(theta),
            y + 0.5 * escala + 0.5 * escala * np.sin(theta)
        )

    elif letra == "E":
        plt.plot(
            [x, x, x + 0.8 * escala],
            [y, y + 1 * escala, y + 1 * escala]
        )

        plt.plot(
            [x, x + 0.7 * escala],
            [y + 0.5 * escala, y + 0.5 * escala]
        )

        plt.plot(
            [x, x + 0.8 * escala],
            [y, y]
        )

    elif letra == "F":
        plt.plot(
            [x, x, x + 0.8 * escala],
            [y, y + 1 * escala, y + 1 * escala]
        )

        plt.plot(
            [x, x + 0.6 * escala],
            [y + 0.5 * escala, y + 0.5 * escala]
        )

    elif letra == "G":

        theta = np.linspace(
            np.pi / 4,
            2 * np.pi + np.pi / 4,
            80
        )

        plt.plot(
            x + 0.5 * escala + 0.5 * escala * np.cos(theta),
            y + 0.5 * escala + 0.5 * escala * np.sin(theta)
        )

        plt.plot(
            [x + 0.5 * escala, x + 1 * escala],
            [y + 0.5 * escala, y + 0.5 * escala]
        )

    elif letra == "I":
        plt.plot(
            [x + 0.5 * escala, x + 0.5 * escala],
            [y, y + 1 * escala]
        )

    elif letra == "L":
        plt.plot(
            [x, x, x + 0.8 * escala],
            [y + 1 * escala, y, y]
        )

    elif letra == "N":
        plt.plot(
            [x, x, x + 0.8 * escala, x + 0.8 * escala],
            [y, y + 1 * escala, y, y + 1 * escala]
        )

    elif letra == "O":

        theta = np.linspace(0, 2 * np.pi, 80)

        plt.plot(
            x + 0.5 * escala + 0.5 * escala * np.cos(theta),
            y + 0.5 * escala + 0.5 * escala * np.sin(theta)
        )

    elif letra == "S":

        theta = np.linspace(
            np.pi / 2,
            3 * np.pi / 2,
            40
        )

        plt.plot(
            x + 0.5 * escala + 0.5 * escala * np.cos(theta),
            y + 0.75 * escala + 0.25 * escala * np.sin(theta)
        )

        theta = np.linspace(
            -np.pi / 2,
            np.pi / 2,
            40
        )

        plt.plot(
            x + 0.5 * escala + 0.5 * escala * np.cos(theta),
            y + 0.25 * escala + 0.25 * escala * np.sin(theta)
        )

    elif letra == "T":

        plt.plot(
            [x, x + 1 * escala],
            [y + 1 * escala, y + 1 * escala]
        )

        plt.plot(
            [x + 0.5 * escala, x + 0.5 * escala],
            [y, y + 1 * escala]
        )

    elif letra == "U":

        plt.plot(
            [x, x],
            [y + 1 * escala, y + 0.3 * escala]
        )

        theta = np.linspace(
            np.pi,
            2 * np.pi,
            40
        )

        plt.plot(
            x + 0.4 * escala - 0.4 * escala * np.cos(theta),
            y + 0.3 * escala + 0.3 * escala * np.sin(theta)
        )

        plt.plot(
            [x + 0.8 * escala, x + 0.8 * escala],
            [y + 0.3 * escala, y + 1 * escala]
        )

    elif letra == "V":

        plt.plot(
            [x, x + 0.5 * escala, x + 1 * escala],
            [y + 1 * escala, y, y + 1 * escala]
        )


# Función para dibujar un nombre
def dibujar_nombre(nombre, x, y, escala=1):

    posicion_x = x

    for letra in nombre:

        dibujar_letra(
            letra,
            posicion_x,
            y,
            escala
        )

        posicion_x += 1.2 * escala


# ==========================================
# DIBUJAR LOS NOMBRES
# ==========================================

plt.figure(figsize=(12, 10))


dibujar_nombre("SOFIA", 0, 8, 1)

dibujar_nombre("LUIS", 0, 6, 1)

dibujar_nombre("STEVE", 0, 4, 1)

dibujar_nombre("NICO", 0, 2, 1)

dibujar_nombre("DIEGO", 0, 0, 1)


# ==========================================
# CONFIGURACIÓN DE LA GRÁFICA
# ==========================================

plt.title("Nombres de los integrantes del grupo")

plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

plt.axis("equal")
plt.grid(True)

plt.show()