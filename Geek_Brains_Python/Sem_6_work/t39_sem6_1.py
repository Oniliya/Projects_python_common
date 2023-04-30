# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random
def create_rand_list(len_list :int) -> list:
    res_list=list()
    for i in range(len_list):
        res_list.append(random.randint(0, 15))
    return res_list

def main():
    len_1_n=int(input("Введите количество элементов первого списка -> "))
    list_1=create_rand_list(len_1_n)
    print(list_1)
    len_2_m=int(input("Введите количество элементов второго списка -> "))
    list_2=create_rand_list(len_2_m)
    print(list_2)

    list_2_set=set(list_2)

    for i in range(len_1_n):
        if not list_1[i] in list_2_set :
            print(list_1[i], end=" ")


main()