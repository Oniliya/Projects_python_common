# __
# Функции высшего порядка: Создайте функцию высшего порядка, которая принимает другую функцию и список чисел. 
# Функция высшего порядка должна возвращать список, содержащий результаты применения переданной функции к каждому элементу списка.


def hight_function(numbers: list, function):
    results = []
    for number in numbers:
        result = function(number)
        results.append(result)
    return results

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = hight_function(numbers, square)
print(squared_numbers)
