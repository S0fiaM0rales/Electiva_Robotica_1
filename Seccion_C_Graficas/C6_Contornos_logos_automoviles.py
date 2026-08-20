import cv2
import matplotlib.pyplot as plt

# Cargar imágenes
logo1 = cv2.imread("logo1.png")
logo2 = cv2.imread("logo2.png")


# Convertir a escala de grises
gris1 = cv2.cvtColor(
    logo1,
    cv2.COLOR_BGR2GRAY
)

gris2 = cv2.cvtColor(
    logo2,
    cv2.COLOR_BGR2GRAY
)


# Convertir a blanco y negro
_, binario1 = cv2.threshold(
    gris1,
    127,
    255,
    cv2.THRESH_BINARY
)

_, binario2 = cv2.threshold(
    gris2,
    127,
    255,
    cv2.THRESH_BINARY
)


# Obtener contornos
contornos1, _ = cv2.findContours(
    binario1,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contornos2, _ = cv2.findContours(
    binario2,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


# GRÁFICA
plt.figure(figsize=(10, 5))


# Logo 1
for contorno in contornos1:

    coordenadas = contorno[:, 0, :]

    x = coordenadas[:, 0]
    y = -coordenadas[:, 1]

    plt.plot(x, y)


# Logo 2
for contorno in contornos2:

    coordenadas = contorno[:, 0, :]

    x = coordenadas[:, 0]
    y = -coordenadas[:, 1]

    plt.plot(x, y)


plt.title("Contornos de logos de automóviles")

plt.xlabel("X")
plt.ylabel("Y")

plt.axis("equal")
plt.grid()

plt.show()