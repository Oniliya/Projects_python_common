# Контекст
# Предположим, что мы хотим найти элемент в массиве (получить
# его индекс). Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно
# использовать бинарный поиск. Принцип прост: сначала берём
# элемент находящийся посередине и сравниваем с тем, который мы
# хотим найти. Если центральный элемент больше нашего,
# рассматриваем массив слева от центрального, а если больше -
# справа и повторяем так до тех пор, пока не найдем наш элемент.

# ● Ваша задача
# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

from random import randint

def find(value:int, my_list: list) -> int:
    left = 0
    right = len(my_list) - 1
    center = (left + right) // 2
    index = -1
    while my_list[center] != value:
        if value > my_list[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2
        if left >= right:
            break
    if value == my_list[center]:
        index=center
    return index

def create_list() -> list:
    my_list={randint(1, 50) for i in range(20)}
    my_list=list(my_list)
    my_list.sort()    
    return my_list


my_list=create_list()
print(my_list)

number=int(input("введите число для поиска в массиве= "))
print(find(number, my_list))
