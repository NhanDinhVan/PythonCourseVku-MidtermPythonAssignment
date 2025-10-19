import math

# Input edges
e1 = float(input("Enter edge 1: "))
e2 = float(input("Enter edge 2: "))

# Input angle in degrees
c_deg = float(input("Enter the third angle (in degrees): "))

# Convert degrees to radians
c = math.radians(c_deg)

# Calculate area using formula 1/2 * a * b * sin(C)
area_exp7 = 0.5 * e1 * e2 * math.sin(c)

print("Area of the triangle is:", area_exp7)
