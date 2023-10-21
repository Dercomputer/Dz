def fib(n):
    a = [0, 1]
    for _ in range(n - 2):
        a.append(a[-2] + a[-1])
    return a[:n]


n = int(input("Число: "))
print(fib(n))
