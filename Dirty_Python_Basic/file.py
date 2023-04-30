# w - write Запись (создание файла)
# r - read Чтение
# a - append Дополнение

# path='file.txt'
# flag = 
# encoding='UTF-8' для винды

# file = open(path, flag, encoding='UTF-8')

# file = open('Data/file.txt', 'w', encoding='UTF-8')
# file = open('Data/file.txt', 'a', encoding='UTF-8')
# file.write('12453\n')
# file.write("sfdsdf\t")
# file.write("воыа")
# file.write("\n")
# file.close()

# file = open('Data/file.txt', 'r', encoding='UTF-8')

# with file = open('Data/file.txt', 'r', encoding='UTF-8') as file:
# остальное с отступом
# close не нужно
PATH='Data/file.txt'
JSON_PATH='Data/text.json'

import json

with open(PATH, 'r', encoding='UTF-8') as file:
    phone_book = file.readlines()

print(phone_book)
new_book={}
for i, contact in enumerate(phone_book, 1):
    contact = contact.strip().split(';')
    new_book[i] = {'name': contact[0], 'phone': contact[1], 'comment':contact[2]}

print(new_book.get(1).get('name'))
print(new_book.get(3).get('name'))



with open(JSON_PATH, 'w', encoding='UTF-8') as file:
    json.dump(new_book, file, ensure_ascii=False)


with open(JSON_PATH, 'r', encoding='UTF-8') as file:
    json_data = json.load(file)

print(type(json_data))
print(json_data)






# file.close()

# data=file.read()

# data_list=[]

# file.seek

# while True:
#     elem=file.readline()
#     if elem != "":
#         data_list.append(elem)
#     else:
#         break

# data_list=file.readlines()

# data=file.readlines()

# data1=file.readline()
# data2=file.readline()
# data3=file.readline()
# data4=file.readline()

# print(file)



# print(data_list)

# print('\n')
# print(data)

# print(data1.__repr__()).__repr__()
# print(data2.__repr__())
# print(data3.__repr__())
# print(data4.__repr__())

# my_list=[data]
# print(my_list)

