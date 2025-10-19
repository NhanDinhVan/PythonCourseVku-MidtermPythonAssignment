data = "helloWorld@gmail.com"

position = data.find("@")
host = data[position + 1:]

print("Host: ", host)