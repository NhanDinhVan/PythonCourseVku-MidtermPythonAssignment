filename = 'alice.txt' 

try:
    with open(filename, 'r', encoding='utf-8') as f_obj:
        contents = f_obj.read()
        print(contents)

except FileNotFoundError:
    msg = f"File '{filename}' không tồn tại hoặc đường dẫn không đúng."
    print(msg)
