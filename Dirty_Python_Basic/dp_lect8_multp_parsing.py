# парсинг многочлена (наверное)
# поиск логических единиц, завершенных для разбиения на информацию, которые можно распознать и заменить
# поиск последовательностей

# задание с ГБ (прошлых потоков)

# задается максимальная степень многочлена (от максимума к минимуму)
# вводим число 
# два многочлена
# сложить (сложить коэфффициенты при равных степенях х)

import random

def create_dict() -> dict[int, int]:
    degree = 14 #int(input('Введите максимальную степень = '))
    my_dict={}
    for k in range(degree, -1, -1):
        my_dict[k]=random.randint(0,5)
    return my_dict

# print(eq_1 :=create_dict())
eq_1=create_dict()
eq_2=create_dict()

def create_equation(eq: dict [int, int]) -> str:
    final=[]
    final_str=''
    for degree, koef in eq.items():
        final_str += f'{koef}*x**{degree}' + ' + ' if koef !=0 else ''

    final_str = (final_str
                 .replace('1*', '', 1)
                 .replace(' 1*', ' ')
                 .replace('1x', 'x')
                 .replace('x**1 ', 'x ')
                 .replace('*x**0', '')
                 .replace(' x**0', ' 1')
                 )
    

    return final_str.rstrip(' + ') + ' = 0'

print(str1 := create_equation(eq_1))
print(str2 := create_equation(eq_2))

def str_to_dict(eq: str) -> dict[int, int]:

    if eq[0]=='x':
        eq=eq.replace('x*', '1*x*', 1)

    eq=eq.replace(' = 0', '').replace(' x**', ' 1*x**').split(' + ')
    new_eq=[]
    
    for elem in eq:
        if elem.isdigit():
            new_eq.append([elem, 0])
        elif elem=='x':
            new_eq.append([1, 1])
        elif elem.endswith('x'):
            new_eq.append([elem.replace('*x', ''), 1])
        else:
            new_eq.append(elem.split('*x**'))
    return {int(degree): int(koef) for koef, degree in new_eq}

# print(dict1 := str_to_dict(str1))
# print(dict2 := str_to_dict(str2))
dict1 = str_to_dict(str1)
dict2 = str_to_dict(str2)

def summ_dict(eq1: dict, eq2: dict) -> dict:
    new_eq = {}
    new_eq.update(eq1)
    new_eq.update(eq2)
    for key in new_eq:
        new_eq[key] = eq1.get(key, 0) + eq2.get(key, 0)

    return dict(sorted(new_eq.items(),reverse=True))

print(create_equation(summ_dict(dict1, dict2)))

