# ДЗ до среды (ну вообще до следующего воскресенья):

# 1. Реализовать алгоритм RLE (упрощенный - это на случай вдруг вы полезете в Wiki)
# что такое RLE? алгоритм сжатия данных, например
# ssssdddfffffgggggggghhkkk -> 4s3d5f8g2h3k
# запаковка и распаковка в обратную сторону
# делаем файл с рандомно созданными строками (как запакованными, так и распакованными)
# считываем файл функция определяет - запакована строка или распакована
# и выполнить соответствующий алгоритм - результаты записать в новый файл

# создать файл
PATH="Data\sample.txt"
PATH_1="Data\sample3.txt"
PATH_2="Data\sample4.txt"

import string
import random

def code_str(str_to_code: str) -> str:
    tmp_str=''

    item=str_to_code[0]
    count=0
    for j in range(len(str_to_code)):
        if item == str_to_code[j]:
            count+=1
        else:
            tmp_str=tmp_str+str(count)+item
            item= str_to_code[j]
            count=1
    return tmp_str+str(count)+item

def decode_str(str_to_decode: str) -> str:
    str_to_write=''
    tmp_str=''
    for i in range(len(str_to_decode)):
        if str_to_decode[i] in '0123456789':
            tmp_str=tmp_str+str_to_decode[i]
        else:
            if tmp_str!='':
                str_to_write=str_to_write+str_to_decode[i]*int(tmp_str)
            tmp_str=''
    return str_to_write

def main():
    read_file_str=''
    with open(PATH, 'w', encoding='UTF-8') as file:
        letters = string.ascii_lowercase
        for i in range(10):
            rand_string = ''.join(random.choice(letters)*random.randint(1,11) for i in range(50))
            print(rand_string, file=file)
        
    with open(PATH, 'r', encoding='UTF-8') as file:
        read_file_str =file.read()

    with open(PATH_1, 'w', encoding='UTF-8') as file:
        new_file_str="".join(c for c in read_file_str if c.isalpha())
        print(code_str(new_file_str),file=file)

    with open(PATH_1, 'r', encoding='UTF-8') as file:
        file_str =file.read()
   
    with open(PATH_2, 'w', encoding='UTF-8') as file:
        print(decode_str(file_str),file=file)
    
main()