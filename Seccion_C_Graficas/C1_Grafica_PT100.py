import numpy as np
import matplotlib.pyplot as plt

# Parámetros del PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Temperatura de -200 °C a 200 °C
temperatura = np.linspace(-200, 200, 1000)

# Vector para almacenar la resistencia
resistencia = np.zeros(len(temperatura))


# Cálculo de resistencia
for i in range(len(temperatura)):

    T = temperatura[i]

    if T < 0:

        resistencia[i] = R0 * (
            1
            + A*T
            + B*T**2
            + C*(T - 100)*T**3
        )

    else:

        resistencia[i] = R0 * (
            1
            + A*T
            + B*T**2
        )


# GRÁFICA
plt.plot(temperatura, resistencia)

plt.title("Comportamiento de un sensor PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ω)")

plt.grid()

plt.show()