# Упражнение 4. Площадь садового участка
# (Решено. 15 строк)
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# Подсказка. В одном акре содержится 43 560 квадратных футов.

width=int(input("Введите длинну участка в футах -> "))
lenght=int(input('Введите длинну участка в футах -> '))
print(f'площадь участка равна {width*lenght/43560} акров')