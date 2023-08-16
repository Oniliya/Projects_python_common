# Дополнительные сложные задачи (по желанию):

# Императивное программирование:

# Задача 6: Упорядочивание списка. Напишите программу, которая сортирует список чисел в порядке возрастания с использованием пузырьковой сортировки или другого метода сортировки.


def sort_list(my_list : list) -> list:
    for i in range(0, len(my_list)):
        for j in range(i,len(my_list)):
            if my_list[j]< my_list[i]:
                temp=my_list[j]
                my_list[j]=my_list[i]
                my_list[i]=temp
    return my_list

print(sort_list(my_list=[0, 5, 43, 25, 2, -2, 0, 15, 3, 54, 4, -2]))


