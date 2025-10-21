# Bài 36: Đọc các số nguyên từ người dùng đến khi nhập 0, rồi sắp xếp

numbers = []

while True:
    n = int(input("Nhập số nguyên (0 để dừng): "))
    if n == 0:
        break
    numbers.append(n)

numbers.sort()  # hoặc dùng: sorted(numbers)

print("\nCác số theo thứ tự tăng dần:")
for num in numbers:
    print(num)
