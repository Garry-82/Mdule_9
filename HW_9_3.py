first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)


first_result = (len(x[0]) - len(x[1]) for x in zp if len(x[0]) != len(x[1]))

second_result = (bool(len(first[x]) == len(second[x])) for x in range(len(first)))

print(list(first_result))
print(list(second_result))