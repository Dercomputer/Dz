x = input("Ввод: ")
list = []


def funk(x):
    while x:
        list.append(x)
        x = input("Ввод: ")
    lst = []
    print("Элемент | Частота")
    for t in list:
        if t not in lst:
            print(t, "|", list.count(t))
            lst.append(t)


funk(x)
