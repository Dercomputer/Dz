n = int(input())


def progress(n):
    s = ((n - (n - 1) + n) / 2) * n
    print(s)


progress(n)
