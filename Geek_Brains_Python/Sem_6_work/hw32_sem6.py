# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random
def create_list(len_list : int) -> list:
    res_list=list()
    for i in range(len_list):
        res_list.append(random.randint(-15, 15))
    return res_list

def main():
    my_len=int(input("Введите количество элементов списка -> "))
    my_list=create_list(my_len)
    print(my_list)

    my_min=int(input("Ведите ваш минимум -> "))
    my_max=int(input("Введите ваш максимум -> "))

    for i in range(len(my_list)):
        if my_min<my_list[i]<my_max :
            print(i, end=" ")

main()