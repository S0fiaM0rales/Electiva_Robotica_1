import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Coeficientes ingresados por teclado
b0 = float(input("Ingrese el coeficiente del numerador: "))

a2 = float(input("Ingrese el coeficiente de s^2: "))
a1 = float(input("Ingrese el coeficiente de s: "))
a0 = float(input("Ingrese el término independiente: "))

# Función de transferencia
numerador = [b0]
denominador = [a2, a1, a0]

sistema = signal.TransferFunction(
    numerador,
    denominador
)

# Cálculo del discriminante
discriminante = a1**2 - 4*a2*a0


# Tipo de sistema
if discriminante < 0:

    tipo_sistema = "Subamortiguado"

elif discriminante == 0:

    tipo_sistema = "Críticamente amortiguado"

else:

    tipo_sistema = "Sobreamortiguado"


# Respuesta al escalón
tiempo, respuesta = signal.step(sistema)


# RESULTADOS
print("\nCoeficientes del sistema:")
print("Numerador:", numerador)
print("Denominador:", denominador)

print("\nDiscriminante:")
print(discriminante)

print("\nTipo de sistema:")
print(tipo_sistema)


# GRÁFICA
plt.plot(tiempo, respuesta)

plt.title("Respuesta al escalón - " + tipo_sistema)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.grid()

plt.show()