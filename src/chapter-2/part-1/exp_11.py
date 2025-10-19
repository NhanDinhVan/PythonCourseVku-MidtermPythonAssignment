# Constant: 1 acre = 4046.86 square meters
ACRE = 43560.00

length = float(input("Enter the length of the field (in meters): "))
width = float(input("Enter the width of the field (in meters): "))

area_square_meters = length * width
area_acres = area_square_meters / ACRE

print(f"The area of the field is: {area_acres:.2f} acres")
