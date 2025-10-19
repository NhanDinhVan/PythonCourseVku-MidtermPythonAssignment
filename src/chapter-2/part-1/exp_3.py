data = 'helloWorld@gmail.com|Sat|Jan|5|09:14:16'

startPosition = data.find("@")
endPosition = data.find('|', startPosition)

host = data[startPosition + 1:endPosition]

print("Host: ", host)