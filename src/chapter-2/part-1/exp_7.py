import math
c1 = float(input("Enter edge 1: "))
c2 = float(input("Enter edge 2: "))

c = float(input("Enter the third angle (in degrees): ")) 

area = 0.5 * (c1 * c2 * math.sin(math.radians(c)))

print("Area of the triangle is: ", area)