import numpy as np
import matplotlib.pyplot as plt

# Datos ingresados por teclado
voltaje = float(input("Ingrese el voltaje (V): "))
capacitancia = float(input("Ingrese la capacitancia (uF): "))
resistencia = float(input("Ingrese la resistencia (ohm): "))

# Conversión de microfaradios a faradios
capacitancia = capacitancia * 10**-6

# Constante de tiempo
tau = resistencia * capacitancia

# Tiempo de simulación
tiempo = np.linspace(0, 5*tau, 500)

# Carga del capacitor
carga = voltaje * (
    1 - np.exp(-tiempo/tau)
)

# Descarga del capacitor
descarga = voltaje * (
    np.exp(-tiempo/tau)
)


# RESULTADOS
print("\nVoltaje:", voltaje, "V")
print("Capacitancia:", capacitancia, "F")
print("Resistencia:", resistencia, "ohm")
print("Constante de tiempo:", tau, "s")


# GRÁFICA
plt.plot(tiempo, carga, label="Carga")
plt.plot(tiempo, descarga, label="Descarga")

plt.title("Carga y descarga de un circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")

plt.grid()
plt.legend()

plt.show()