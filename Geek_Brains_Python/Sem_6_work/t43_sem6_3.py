# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

import random

def create_list(len_list: int)-> list:
    res_list=list()
    for i in range(len_list):
        res_list.append(random.randint(0, 10))
    return res_list

def main():
    my_len=int(input("Введите количество элементов списка -> "))
    my_list=create_list(my_len)
    print(my_list)

    count=0

    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i]==my_list[j]:
                count+=1
                
    
    print(f"количество пар элементов, равных друг другу = {count}")

main()