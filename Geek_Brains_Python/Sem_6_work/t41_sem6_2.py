# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

import random
def create_list(len_list :int) -> list:
    res_list=list()
    for i in range(len_list):
        res_list.append(random.randint(0, 15))
    return res_list

def main():
    my_len=int(input("Введите количество элементов списка -> "))
    my_list=create_list(my_len)
    print(my_list)

    count=0
    for i in range(1,my_len-1):
        if my_list[i-1]<my_list[i] and my_list[i]>my_list[i+1]:
            count+=1
    print(f"количество элементов, у которых оба соседних меньше = {count} ")

main()