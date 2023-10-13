def maxnumber(a):
    m = len(max(a, key=len))
    a.sort(key=lambda x: x * m, reverse=True)
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
