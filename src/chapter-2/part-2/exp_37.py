# Bài 37: Đọc các từ cho đến khi gặp dòng trống và loại bỏ từ trùng

words = []  # Danh sách lưu các từ (theo thứ tự nhập)

print("Nhập các từ (nhấn Enter trên dòng trống để kết thúc):")

while True:
    word = input("> ").strip()
    if word == "":
        break  # Dừng khi người dùng nhập dòng trống
    if word not in words:
        words.append(word)  # Chỉ thêm nếu từ chưa có trong danh sách

print("\nCác từ sau khi loại bỏ trùng lặp:")
for w in words:
    print(w)
