x = input("Введите данные или оставить поле пустым для завершения: ")
list = []
while x != "":
    list.append(x) 
    # Добавляем в конец списка нужные данные
    x = input("Введите данные или оставить поле пустым для завершения: ")
print("Итоговый список", list)
