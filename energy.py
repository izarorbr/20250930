# e = m * C**2

c = 299792458  # velocidad de la luz en m/s
print(f"La velocidad de la luz es {c} m/s")

mass = int(input("Indica la masa en kilogramos: "))
energy = mass * c**2

print(f"La energía para una masas de {mass} kg es {energy} Julios.")
