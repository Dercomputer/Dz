n = int(input("Число: "))


def fib(n):
    a = 1
    b = 1
    lst = [a, b]
    for i in range(2, n):
        a, b = b, a + b
        lst.append(b)
    return (lst)


print(fib(n))
