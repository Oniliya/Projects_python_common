# Обязательные задачи:

# Императивное программирование:
# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.

def sum_n(n: int) -> int:
    summa = 0
    for i in range(1, n+1):
        summa +=i
    return summa

n=int(input("введите число = "))
print(sum_n(n))

