a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))
f = float(input("Введите число f: "))
if f-d != 0:
    r = (a * b - c)/(f - d)
    print(r)
else:
    print("Делить на ноль нельзя!")