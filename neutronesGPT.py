import random
import numpy as np

# Parámetros de entrada
num_neutrones = int(input("Ingresa el número de neutrones a simular: "))
densidad_material = float(input("Ingresa la densidad del material en g/cm^3: "))
espesor_material = float(input("Ingresa el espesor del material en cm: "))

# Constantes físicas
mac_neutrones = 2.33 # cm^2/g

# Contadores
neutrones_absorb = 0

for i in range(num_neutrones):
    # Generar posición inicial aleatoria del neutrón
    x = random.uniform(0, espesor_material)
    y = random.uniform(0, espesor_material)
    z = random.uniform(0, espesor_material)

    # Generar dirección inicial aleatoria del neutrón
    direccion_x = random.uniform(-1, 1)
    direccion_y = random.uniform(-1, 1)
    direccion_z = random.uniform(-1, 1)

    # Calcular la distancia recorrida antes de ser absorbido
    dist_recorrida = -(1/mac_neutrones) * np.log(random.uniform(0, 1))
    x += dist_recorrida * direccion_x
    y += dist_recorrida * direccion_y
    z += dist_recorrida * direccion_z

    # Verificar si el neutrón fue absorbido dentro del material
    if x > 0 and x < espesor_material and y > 0 and y < espesor_material and z > 0 and z < espesor_material:
        neutrones_absorb += 1

# Calcular la fluencia de neutrones absorbida
fluencia_neutrones = neutrones_absorb / (espesor_material * espesor_material * espesor_material * densidad_material)
print("La fluencia de neutrones absorbida es: ", fluencia_neutrones, "neutrones/cm^2")