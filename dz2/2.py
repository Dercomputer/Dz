spicok = []
a = input("Вводите числа по одному и без пробелов(в начале и конце). "
          "Для перехода к результату введите пустую строку: ")
while a:
    spicok.append(a)
    a = input("Вводите числа по одному и без пробелов(в начале и конце). "
              "Для перехода к результату введите пустую строку: ")
spicok.sort(reverse=True)
print("".join(spicok))