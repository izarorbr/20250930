# Kinetic Energy (KE) = 0.5 * mass * velocity^2

mass = float(input("Enter the mass in kilograms: "))
velocity = float(input("Enter the velocity (in m/s): "))
kinetic_energy = (0.5 * mass * velocity**2)

message = f"La energía cinética es de {kinetic_energy} Julios."
print(message)
