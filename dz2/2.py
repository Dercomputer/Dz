# На паре хотел бы вот это разобрать и шестое. Думаю просто есть решение проще
spicok = []
a = input("Вводите числа по одному и без пробелов(в начале и конце). "
          "Для перехода к результату введите пустую строку: ")
while a != "":
    spicok.append(a)
    a = input("Вводите числа по одному и без пробелов(в начале и конце). "
              "Для перехода к результату введите пустую строку: ")
else:
    spicok = sorted(spicok, reverse = True) 
    string = ""
    for t in spicok:
        string = string + t 
        # Применяем sorted, чтобы на выходе получить список уже отсортированный, 
        # reverse - переворачивает список, поэтому сначала идут большие числа
        # Далее создаём пустую строку в которую будем переводить наш список
        # С помощью цикла for переводим каждый элемент списка в строку и складываем
        # Есть подозрение, что это можно сделать гораздо проще, но я не придумал как))
    print(string)