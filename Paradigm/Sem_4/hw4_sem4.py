# Функция-редуктор: Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список чисел, 
# а затем возвращает произведение всех чисел в списке. Используйте эту функцию для вычисления произведения чисел в списке.


import functools

def multip_list(start: int, numbers: list) -> int:
    return functools.reduce(lambda x,y : x*y, numbers, start)



print(multip_list(start=1, numbers=[3,4,5]))