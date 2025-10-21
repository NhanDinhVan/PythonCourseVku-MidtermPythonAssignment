
n = int(input("Nhập một số thập phân: "))

binary = ""
temp = n

if n == 0:
    binary = "0"
else:
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

print(f"Số nhị phân tương ứng với {temp} là: {binary}")
