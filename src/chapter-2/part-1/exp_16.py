import math

g = 9.8 

height = float(input("Enter the height (meters): "))

v_final = math.sqrt(2 * g * height)

print(f"\nThe final velocity when the object hits the ground is: {v_final:.2f} m/s")
