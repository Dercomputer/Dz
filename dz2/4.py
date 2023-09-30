stroka = input("Введите произвольную строку со скобками: ")
x = stroka.count("(") 
y = stroka.count(")")
if x > y:
    print("Не хватает", x - y, "закрывающих скобок")
elif x < y:
    print("Не хватает", y - x, "открывающих скобок")
else:
    print("Всё на месте")
