# Обязательные задачи:


# Декларативное программирование:
# Задача 4: Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.


def find_unic(my_list: list) -> set:
    return set(my_list)

print(find_unic(my_list=[0, 5, 43, 25, 2, -2, 0, 15, 3, 54, 4, -2]))

