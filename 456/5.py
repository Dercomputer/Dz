x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка лежит в первой четверти")
elif x > 0 and y < 0:
    print("Точка лежит в четвёртой четверти")
elif x < 0 and y < 0:
    print("Точка лежит в третьей четверти")
elif x < 0 and y > 0:
    print("Точка лежит во второй четверти")
elif x == 0 and y != 0:
    print("Точка лежит на оси x")
elif x != 0 and y == 0:
    print("Точка лежит на оси y")
else:
    print("Точка находится в начале координат")
