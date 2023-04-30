# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

def main():
    import random

    count_first_list=int(input("Введите количество элементов первого набора -> "),)
    count_second_list=int(input("Введите количество элементов первого набора -> "),)
    first_list=[]
    for i in range(count_first_list):
        first_list.append(random.randint(0,15))
    print(first_list)
    second_list=[]
    for i in range(count_second_list):
        second_list.append(random.randint(0,15))
    print(second_list)

    first_set=set(first_list)
    second_set=set(second_list)
    
    print(sorted(first_set.intersection(second_set)))
    

main()