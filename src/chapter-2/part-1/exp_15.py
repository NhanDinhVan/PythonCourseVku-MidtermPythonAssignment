# Constants
C = 4.186            
J_TO_KWH = 2.777e-7    
COST_PER_KWH = 8.9     

# Input
mass = float(input("Enter the mass of water (grams): "))
delta_T = float(input("Enter the temperature change (°C): "))

# Calculate energy (in Joules)
Q = mass * C * delta_T

# Convert to kWh
Q_kWh = Q * J_TO_KWH

# Calculate cost
cost = Q_kWh * COST_PER_KWH

# Output
print("\nResults:")
print(f"Energy required: {Q:.2f} Joules")
print(f"Energy in kWh: {Q_kWh:.6f} kWh")
print(f"Heating cost: {cost:.4f} cents")
