# Bài 48: Tính giá trị trung bình của 3 số

def average(a, b, c):
    """Hàm tính trung bình của 3 số"""
    return (a + b + c) / 3

# Chương trình chính
x = float(input("Nhập số thứ nhất: "))
y = float(input("Nhập số thứ hai: "))
z = float(input("Nhập số thứ ba: "))

print(f"Giá trị trung bình của 3 số là: {average(x, y, z)}")
