
# Дополнительные сложные задачи (по желанию):

# Декларативное программирование:
# Задача 7: Поиск подстроки. Напишите программу, которая находит все вхождения заданной подстроки в строке с использованием встроенных функций.


import re

def find_str(my_str: str, f_str: str) ->list:
    return [st.start() for st in re.finditer(f_str, my_str)] 

my_str1=input('введите строку ')
my_str2=input('введите подстроку ')

print(find_str(my_str1.lower(), my_str2.lower()))

