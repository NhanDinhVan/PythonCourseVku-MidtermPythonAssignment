
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)

except FileNotFoundError:
    msg = "File '" + filename + "' không tồn tại hoặc đường dẫn không đúng."
    print(msg)
