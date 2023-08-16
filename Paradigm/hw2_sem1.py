# Обязательные задачи:

# Императивное программирование:
# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.



def find_min(my_list: list) -> int:
    min_list = my_list[0]
    for num in my_list:
        if num< min_list:
            min_list=num
    return min_list

print(find_min(my_list = [0, 5, 43, 25, 2, -2]))