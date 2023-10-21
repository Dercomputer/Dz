def unik(x):
    return len(x) == len(set(x))


if __name__ == '__main__':
    print(unik(input().split()))