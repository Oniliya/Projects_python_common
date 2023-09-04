# Функции-редуцеры для списков: Напишите функцию-редуктор, которая принимает список строк и возвращает строку, 
# состоящую из объединенных элементов списка через запятую. Например, для списка ["apple", "banana", "cherry"] 
# результат должен быть "apple, banana, cherry".



import functools

def reduce_list(words: list) -> str:
    return functools.reduce(lambda x,y : x + ', ' + y, words)



print(reduce_list(words=["apple", "banana", "cherry"]))