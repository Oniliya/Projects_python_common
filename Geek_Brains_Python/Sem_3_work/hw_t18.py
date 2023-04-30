# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n=int(input("введите количество элементов = "))
a=[]
for i in range(n):
    a.append(random.randint(-5,15))
print(a)

x=int(input("Введите ваше число = "))
nearest_digit=a[0]
nearest_digit_difference=abs(a[0]-x)

for i in range(len(a)):
    if abs(a[i]-x) < nearest_digit_difference: 
        nearest_digit_difference=abs(a[i]-x)
        nearest_digit=a[i]
    
print(nearest_digit)