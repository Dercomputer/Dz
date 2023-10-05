def f(lst):
    itog = []
    for i in lst:
        a = int(i)
        itog.append(a)
    y = sum(itog) / len(itog)
    print(y)


lst = input().split()
f(lst)
