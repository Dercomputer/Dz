x = input("Ввод: ")
list = []


def funk(x):
    while x:
        list.append(x)
        x = input("Ввод: ")
    return list


print(funk(x))
