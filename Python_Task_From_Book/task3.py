# Упражнение 3. Площадь комнаты
# (Решено. 13 строк)
# Напишите программу, запрашивающую у пользователя длину и ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.

width=int(input("Введите ширину комнаты -> "))
length=int(input("Введите длинну комнаты -> "))
print(f"площадь комнаты = {width*length} кв.м")