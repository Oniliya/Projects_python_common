
# Дополнительные сложные задачи (по желанию):

# Императивное программирование:
# Задача 5: Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном диапазоне от 1 до N.


def if_simple(num: int) -> bool:
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True

num = int(input('введите число = '))
for i in range(1, num+1):
    if if_simple(i) : print(i)
