# __
# Чистые функции и неизменяемость данных: Напишите функцию, которая принимает список чисел и возвращает новый список, 
# в котором каждый элемент умножен на 2. Убедитесь, что вы используете только чистые функции и не изменяете исходный список.
# __

def function_new_list(old_list: list)-> list:
    new_list=[]
    for x in old_list:
        new_list.append(x*x)
    return new_list

list1=[1,2,3,4,5]

print(function_new_list(list1))

print(list1)