import cv2
import matplotlib.pyplot as plt

def graficar_contornos(ruta_imagen, titulo):
    # 1. Leer la imagen
    img = cv2.imread(ruta_imagen)
    
    # Verificar si la imagen se cargó correctamente
    if img is None:
        print(f"Error: No se encontró la imagen '{ruta_imagen}'. Verifica que el nombre y la carpeta sean correctos.")
        return

    # 2. Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Aplicar umbralización
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # 4. Encontrar los contornos
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 5. Preparar la gráfica con matplotlib
    plt.figure(figsize=(8, 6))
    plt.title(titulo)

    # 6. Extraer las coordenadas X y Y y graficarlas
    for contorno in contornos:
        x = contorno[:, 0, 0]
        y = contorno[:, 0, 1]
        plt.plot(x, y, linewidth=2)

    # Invertir el eje Y y mantener la proporción
    plt.gca().invert_yaxis()
    plt.axis('equal') 
    plt.grid(True)
    plt.show()

# Ejecutar la función con los nombres nuevos
graficar_contornos('AUDI.png', 'Coordenadas X y Y - Contornos Audi')
graficar_contornos('LOGOC.png', 'Coordenadas X y Y - Contornos Chevrolet')