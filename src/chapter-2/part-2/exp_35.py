# Bài 35: Lọc ra các số lẻ từ danh sách nhập vào

nums = input("Nhập các số, cách nhau bởi dấu phẩy: ")
nums = [int(x) for x in nums.split(",")]

odd_nums = [x for x in nums if x % 2 != 0]

print("Các số lẻ là:", odd_nums)
