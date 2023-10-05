def fib(n):
   a = 1
   b = 1
   for i in range(1, n+1):
    if i == 1 or i == 2:
          print(a)
    elif i > 2:
        a, b = b, a+b
        print(b)
n = int(input("Число: "))
fib(n)
