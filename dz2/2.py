def maxnumber(a):
    a.sort(key=lambda x: x * 3, reverse=True)
    result = ''.join(a)
    result = int(result)
    return result

a = []
while True:
    number = input("Введите число: ")
    if number == '':
        break
    a.append((number))

max_number = maxnumber(a)
print(max_number)
