def lst():
    a = []
    while True:
        number = input()
        if number == '':
            break
        a.append((number))
    return a

def sdvig(a, k):
    k %= len(a)
    return a[-k:] + a[:-k]

if __name__ == "__main__":
    a = lst()
    k = int(input())
    print(sdvig(a, k))
