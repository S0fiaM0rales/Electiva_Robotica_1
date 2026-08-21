import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Ingreso de parámetros estándar por teclado
K = float(input("Ingrese la ganancia estática (K): "))
wn = float(input("Ingrese la frecuencia natural del sistema (ωn): "))
zeta = float(input("Ingrese el factor de amortiguamiento (ζ): "))

# Construcción de la función de transferencia
# G(s) = (K * wn^2) / (s^2 + 2*zeta*wn*s + wn^2)
numerador = [K * (wn**2)]
denominador = [1, 2 * zeta * wn, wn**2]

sistema = signal.TransferFunction(numerador, denominador)

# Tipo de sistema basado directamente en el factor de amortiguamiento (zeta)
if zeta < 1:
    tipo_sistema = "Subamortiguado"
elif zeta == 1:
    tipo_sistema = "Críticamente amortiguado"
else:
    tipo_sistema = "Sobreamortiguado"

# Respuesta al escalón
tiempo, respuesta = signal.step(sistema)

# RESULTADOS
print("\n--- Parámetros ingresados ---")
print(f"Ganancia estática (K): {K}")
print(f"Frecuencia natural (ωn): {wn}")
print(f"Factor de amortiguamiento (ζ): {zeta}")

print("\n--- Polinomios resultantes ---")
print("Numerador:", numerador)
print("Denominador:", denominador)

print("\n--- Tipo de sistema ---")
print(tipo_sistema)

# GRÁFICA
plt.plot(tiempo, respuesta)
plt.title("Respuesta al escalón - " + tipo_sistema)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()
