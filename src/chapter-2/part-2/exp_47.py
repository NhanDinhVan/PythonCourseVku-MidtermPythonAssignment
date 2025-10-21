# Bài 47: In tất cả giá trị của danh sách trừ 5 phần tử đầu tiên

def squares_except_first_five():
    """Hàm tạo danh sách bình phương và in các phần tử trừ 5 phần tử đầu"""
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print("Danh sách trừ 5 phần tử đầu tiên là:")
    print(squares[5:])  # Cắt bỏ 5 phần tử đầu

# Gọi hàm
squares_except_first_five()
