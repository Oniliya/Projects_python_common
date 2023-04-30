# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def reccur_sum(term_1: int, term_2 : int) -> int:
    if term_2==0:
        return term_1
    else:
        return reccur_sum(term_1 +1 ,term_2 -1 )



def main():
    number_a=int(input("Введите первое число = "))
    number_b=int(input("Введите второе число = "))

    print(reccur_sum(number_a, number_b))

main()