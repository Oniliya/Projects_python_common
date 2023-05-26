
# map
# my_string=list(map(функция, коллекция))

# filter

# enumerate
# получим кортеж


# zip
from itertools import zip_longest


# lambda


my_string='1234567890'
my_string=list(my_string)
print(my_string)

# for i in range(len(my_string)):
#     my_string[i]=int(my_string[i])

# my_string=list(map(int, my_string))
# my_string=list(map(lambda x: x +'1', my_string))


my_string='1werwre234567890'
# print(my_string)
# my_string=list(filter(lambda x: not x.isdigit(), my_string))
# print(my_string)


# for i, item in enumerate(my_string, 1):
#     print(i, item)


my_num='12345'
my_let='qwertyuiop'

list_1=list(my_num)
list_2=list(my_let)

# print(list_1)
# print(list_2)

new_list=[]
# for i, item in enumerate(list_1):
#     new_list.append((list_1[i], list_2[i]))

new_list=list(zip(list_1, list_2))
print(new_list)
new_list=list(zip_longest(list_1, list_2, fillvalue='ничего'))
print(new_list)



def is_digit(num:str):
    return num.isdigit()

lambda x: x.isdigit()