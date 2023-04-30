# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300
# Вывод:
# 220 284

import math

def create_divider_sum(number :int) -> int:
    res_list_sum=0
    for i in range (1, number//2+1):
        if number%i==0 :
            res_list_sum+=i
    return res_list_sum

def main():
    number_k=int(input("Введите число -> "))

    for i in range(number_k):
        sum_i=create_divider_sum(i)
        for j in range(i+1, number_k):
            if j==sum_i and i==create_divider_sum(j):
                print(i,j)
    
                
main()





# def divisors_sum(number):
#     return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)


# max_number = 10000
# pairs = {}
# for i in range(1, max_number + 1):
#     aggr = divisors_sum(i)
#     if i == divisors_sum(aggr) and i != aggr:
#         if i and aggr not in pairs:
#             pairs[i] = aggr
# print(pairs)

