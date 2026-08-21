import os
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Limpiar pantalla y cerrar figuras previas
os.system('cls' if os.name == 'nt' else 'clear')
plt.close('all')

def extraer_y_graficar_contornos(ruta_imagen, nombre_logo):
    # 1. Cargar imagen en escala de grises
    img = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Error: No se pudo cargar la imagen '{ruta_imagen}'. Verifica el nombre o ruta.")
        return

    # 2. Binarizar e invertir para resaltar las formas del logo
    # Ajustar según si el fondo es blanco o transparente/oscuro
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

    # 3. Extraer los contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # 4. Graficar los contornos extrayendo sus coordenadas X e Y
    plt.figure(figsize=(8, 6))
    
    total_puntos = 0
    for i, cnt in enumerate(contours):
        # Ignorar contornos extremadamente pequeños (ruido)
        if cv2.contourArea(cnt) > 50:
            # Reorganizar el arreglo de OpenCV para separar coordenadas X e Y
            puntos = cnt.squeeze()
            if len(puntos.shape) == 2:  # Asegurar que sea una matriz bidimensional
                x = puntos[:, 0]
                y = puntos[:, 1]
                
                # Invertir eje Y para que no quede cabeza abajo (OpenCV mide Y de arriba a abajo)
                y = img.shape[0] - y  
                
                plt.plot(x, y, linewidth=1.5)
                total_puntos += len(x)

    plt.title(f'Contornos Extraídos ($X, Y$) - Logo de {nombre_logo}')
    plt.xlabel('Coordenada X (Píxeles)')
    plt.ylabel('Coordenada Y (Píxeles)')
    plt.grid(True)
    plt.axis('equal')
    
    print(f'Logo de {nombre_logo}:')
    print(f' - Contornos significativos detectados: {len(contours)}')
    print(f' - Total de puntos (X, Y) extraídos: {total_puntos}\n')

carpeta_imagenes = Path(__file__).resolve().parent
extraer_y_graficar_contornos(str(carpeta_imagenes / 'mazda.png'), 'Mazda')
extraer_y_graficar_contornos(str(carpeta_imagenes / 'mercedes.jpg'), 'Mercedes-Benz')

plt.show()
