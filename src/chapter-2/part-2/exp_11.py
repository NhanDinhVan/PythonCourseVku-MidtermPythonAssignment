numList = list()
while (True):
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print("Giá trị Trung bình:", average)
print(numList)

