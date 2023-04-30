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

def create_list_divider(number :int) -> list:
    res_list=list()
    for i in range (1, number//2+1):
        if number%i==0 :
            res_list.append(i)
    return res_list

def sum_my_list(my_list :list) ->int:
    my_sum=0
    for i in range(len(my_list)):
        my_sum+=my_list[i]
    return my_sum

def main():
    number_k=int(input("Введите число -> "))
    # print(create_list_divider(number_k))

    for i in range(1, number_k):
        
        for j in range(i+1, number_k):
            if i==sum_my_list(create_list_divider(j)) and sum_my_list(create_list_divider(i))==j :
                # print(create_list_divider(i)," | ",i,j)
                print(i,j)
                
main()

