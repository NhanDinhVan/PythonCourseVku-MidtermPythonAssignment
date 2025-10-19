dinner_total = float(input("Enter the total amount of dinner: "))

tip = dinner_total * 0.18
tax = dinner_total * 0.05

total = dinner_total + tip + tax

print(f"The total amount of the dinner is: $ {total:.2f}")