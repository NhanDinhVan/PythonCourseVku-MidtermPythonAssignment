import math

Ta = float(input("Enter the air temperature (°C): "))
V = float(input("Enter the wind speed (km/h): "))

WCI = 13.12 + 0.6215 * Ta - 11.37 * math.pow(V, 0.16) + 0.3965 * Ta * math.pow(V, 0.16)

WCI_rounded = round(WCI)

print(f"\nThe wind chill index is approximately: {WCI_rounded} °C")
