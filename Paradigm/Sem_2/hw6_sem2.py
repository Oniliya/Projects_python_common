
# Рекурсивное вычисление чисел Фибоначчи:
# __
# Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
# Входные данные:
# Число n.
# Выходные данные:
# n-тое число Фибоначчи.

def fibon(num: int) -> int:
    if num == 0 :
        return 0
    if num == 1 :
        return 1
    return fibon(num-2)+fibon(num-1)


if __name__ == "__main__":
    num = int(input("Введите номер числа Фибоначи = "))
    print(fibon(num))