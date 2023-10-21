def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
