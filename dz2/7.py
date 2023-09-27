from random import randint

x = randint(0, 100) # генерирует случайное число от 1 до 100
y = int(input("Введите число от 1 до 100: "))
while y < 0:
    print("Число отрицательное, введите другое ")
    y = int(input("Введите число от 1 до 100: "))
while y > 0:
    if x > y:
        print("Загаданное число больше!")
        y = int(input("Введите число от 1 до 100: "))
    elif x < y:
        print("Загаданное число меньше!")
        y = int(input("Введите число от 1 до 100: "))
    else:
        print("Вы угадали число!")
        break