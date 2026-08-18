import math

# Coordenadas rectangulares previamente inicializadas
x = 3
y = 4
z = 5

# COORDENADAS CILÍNDRICAS

# Radio
rho = math.sqrt(x**2 + y**2)

# Ángulo azimutal
phi = math.atan2(y, x)

# Conversión de radianes a grados
phi_grados = math.degrees(phi)

# COORDENADAS ESFÉRICAS

# Radio esférico
r = math.sqrt(x**2 + y**2 + z**2)

# Ángulo azimutal
phi_esferico = math.atan2(y, x)

# Ángulo polar
theta = math.acos(z / r)

# Conversión a grados
phi_esferico_grados = math.degrees(phi_esferico)
theta_grados = math.degrees(theta)

# RESULTADOS

print("COORDENADAS RECTANGULARES")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

print("\nCOORDENADAS CILÍNDRICAS")
print(f"ρ = {rho:.4f}")
print(f"φ = {phi_grados:.4f} grados")
print(f"z = {z}")

print("\nCOORDENADAS ESFÉRICAS")
print(f"r = {r:.4f}")
print(f"θ = {theta_grados:.4f} grados")
print(f"φ = {phi_esferico_grados:.4f} grados")
