n = int(input("Число: "))


def prost(n):
    if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0
        or n % 13 == 0) and n not in [2, 3, 5, 7, 11, 13] or n == 1:
        print(False)
    else:
        print(True)


prost(n)
