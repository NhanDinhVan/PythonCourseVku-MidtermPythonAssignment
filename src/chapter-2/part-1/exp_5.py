st = input('Enter your string: ')
first_five_characters = st[:5]
last_five_characters = st[len(st)-5:]
four_str_1_line = 4 * (st + ' ')
four_str_4_line = 4 * (st + '\n')

print("First five characters are: " + first_five_characters)
print("Last five characters are: " + last_five_characters)
print("Four strings of one line are: " + four_str_1_line)
print("Four strings of four line are: \n" + four_str_4_line)
