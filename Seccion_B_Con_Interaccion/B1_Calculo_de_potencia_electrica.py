import numpy as np

# Datos ingresados por teclado
voltaje = float(input("Ingrese el voltaje en voltios: "))
corriente = float(input("Ingrese la corriente en amperios: "))

# Cálculo de potencia
potencia = voltaje * corriente

# RESULTADOS
print("\nVoltaje:", voltaje, "V")
print("Corriente:", corriente, "A")
print("Potencia:", potencia, "W")