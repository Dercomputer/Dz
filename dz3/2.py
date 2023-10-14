def Season(n):
    if n in [1, 2, 12]:
        return "Зима"
    if n in [3, 4, 5]:
        return "Весна"
    if n in [6, 7, 8]:
        return "Лето"
    if n in [9, 10, 11]:
        return "Осень"
    return "Ошибка"

     
n = int(input("Месяц: "))
print(Season(n))
