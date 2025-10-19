import math

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
quot_ab = a / b if b != 0 else "undefined (division by zero)"
mod_ab = a % b if b != 0 else "undefined (modulo by zero)"
log10_a = math.log10(a) if a > 0 else "undefined (log of non-positive number)"
power_ab = a ** b

# Display results
print("\nResults:")
print("Sum (a + b):", sum_ab)
print("Difference (a - b):", diff_ab)
print("Product (a * b):", prod_ab)
print("Quotient (a / b):", quot_ab)
print("Remainder (a % b):", mod_ab)
print("log10(a):", log10_a)
print("a ^ b:", power_ab)
