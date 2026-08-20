import math

# DATOS DEL CILINDRO

# Presión de trabajo
presion_bar = 6

# Diámetro del pistón
diametro_piston_mm = 50

# Diámetro del vástago
diametro_vastago_mm = 20

# CONVERSIÓN DE UNIDADES

# Conversión de bar a Pascal
presion_pa = presion_bar * 100000

# Conversión de milímetros a metros
diametro_piston_m = diametro_piston_mm / 1000
diametro_vastago_m = diametro_vastago_mm / 1000

# CÁLCULO DE ÁREAS

# Área total del pistón
area_piston = math.pi * diametro_piston_m**2 / 4

# Área del vástago
area_vastago = math.pi * diametro_vastago_m**2 / 4

# Área efectiva durante el retroceso
area_retroceso = area_piston - area_vastago

# CÁLCULO DE FUERZAS

# Fuerza de avance
fuerza_avance = presion_pa * area_piston

# Fuerza de retroceso
fuerza_retroceso = presion_pa * area_retroceso

# Conversión de Newton a kgf
fuerza_avance_kgf = fuerza_avance / 9.80665
fuerza_retroceso_kgf = fuerza_retroceso / 9.80665


# RESULTADOS

print("CILINDRO NEUMÁTICO DE DOBLE EFECTO")

print(f"\nPresión de trabajo: {presion_bar} bar")
print(f"Diámetro del pistón: {diametro_piston_mm} mm")
print(f"Diámetro del vástago: {diametro_vastago_mm} mm")

print(f"\nÁrea del pistón: {area_piston:.6f} m²")
print(f"Área del vástago: {area_vastago:.6f} m²")

print("\nFuerza de avance:")
print(f"{fuerza_avance:.2f} N")
print(f"{fuerza_avance_kgf:.2f} kgf")

print("\nFuerza de retroceso:")
print(f"{fuerza_retroceso:.2f} N")
print(f"{fuerza_retroceso_kgf:.2f} kgf")
