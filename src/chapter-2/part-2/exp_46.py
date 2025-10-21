# Bài 46: In 5 phần tử cuối cùng của danh sách bình phương từ 1 đến 20

def last_five_squares():
    """Hàm tạo danh sách bình phương và in 5 phần tử cuối"""
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print("5 phần tử cuối cùng của danh sách bình phương là:")
    print(squares[-5:])  # Cắt danh sách từ cuối

# Gọi hàm
last_five_squares()
