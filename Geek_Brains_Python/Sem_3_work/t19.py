# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

import random

list_count=10

my_list=[]
for i in range(list_count):
    my_list.append(random.randint(1,10)-5)
print(my_list)

k=int(input("введите сдвиг = ",))

my_new_list=my_list[k:]+my_list[:k]

print(my_new_list)