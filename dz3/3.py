def fib(n):
    a = 1
    b = 1
    for i in range(1, n+1):
        if i in [1, 2]:
            print(a, end=" ")
        elif i > 2:
            a, b = b, a+b
            print(b, end=" ")


n = int(input("Число: "))
fib(n)
