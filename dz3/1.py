def vvod(x):
    lst = []
    while x:
        lst.append(x)
        x = input()
    return lst

if __name__ == "__main__":
    x = input("Ввод: ")
    print(vvod(x))
