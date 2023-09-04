# __
# Замыкание: Создайте функцию, которая принимает некоторое число n и возвращает функцию, которая прибавляет n к своему аргументу. 
# Продемонстрируйте использование этой функции-замыкания.
# __

def outer_function(n):
    def inner_function(a):
        return n + a
    return inner_function

closure = outer_function(10)
print(closure(5)) 