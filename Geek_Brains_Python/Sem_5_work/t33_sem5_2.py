# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
def main():
    count_numbers=int(input("Введите количество оценок ученика -> "))
    my_list=[]
    for i in range(count_numbers):
        my_list.append(random.randint(1,5))
    print(my_list)

    my_list_max=max(i for i in my_list)
    my_list_min=min(i for i in my_list)

    my_list_res=[]
    for i in range(count_numbers):
        if my_list[i]==my_list_max:
            my_list_res.append(my_list_min)
        else:
            my_list_res.append(my_list[i])

    print(my_list_res)

main()
