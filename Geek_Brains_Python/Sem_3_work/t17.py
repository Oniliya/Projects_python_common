# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [ 1,1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

list_count=10
my_list=[]
my_count=set()
for i in range(list_count):
    my_list.append(random.randint(1,10)-5)
    my_count.add(my_list[i])

print(my_list)
print(len(my_count))
