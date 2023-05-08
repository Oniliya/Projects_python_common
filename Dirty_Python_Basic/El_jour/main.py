# {физика : {ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],}}
# {химия  : {ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],}}
# {биология : {ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],
#            ФИО:[],}}


# добавить оценку ученику (если ученика нет, то добавится ученик и предмет)

# открытие файла и чтение из него журнала

# создание файла журнала /txt
PATH='el_jour.txt'
PATH1='el_jour.txt'

import string


def read_from_el_jur() ->dict:
    all_dict={}
    with open(PATH, 'r', encoding='UTF-8') as file:
        read_file_list=file.readlines()

    for str_item in read_file_list:
        key , fio_key, marks = str_item.strip().split(' : ')
        if all_dict.get(key,None):
            if all_dict[key].get(fio_key, None):
                all_dict[key][fio_key]+=marks
            else:
                all_dict[key][fio_key]=marks
        else:
            all_dict[key]={fio_key: marks}

    # print(all_dict)
    return all_dict

def write_to_el_jour(my_dict: dict):
    with open(PATH1, 'w', encoding='UTF-8') as file:
        new_file_str=''
        for key, value in my_dict.items():
            for fio_key, marks in value.items():
                new_file_str+=key+' : '+fio_key+' : '+marks
                print(new_file_str,file=file)
                new_file_str=''

def print_dict(my_dict : dict):
    for key, value in my_dict.items():
            new_file_str=''
            for fio_key, marks in value.items():
                new_file_str+=key+' : '+fio_key+' : '+marks
                print(new_file_str)
                new_file_str=''

def add_new_marks(my_dict: dict, fio_str: str, subj: str, marks: str) -> dict:
    new_dict=my_dict
    if new_dict.get(subj, None):
        if new_dict[subj].get(fio_str, None):
            new_dict[subj][fio_str]+=', '+marks
        else:
            new_dict[subj][fio_str]=marks
    else:
        new_dict[subj]={fio_str : marks}

    return new_dict
    

def main():
    el_jour_dict = read_from_el_jur()
    print_dict(el_jour_dict)


    new_str=input('введите ФАМИЛИЮ ИМЯ ученика, ПРЕДМЕТ и оценку или СТОП ')

    while new_str != 'СТОП':
        # print(new_str)
        new_str=new_str.strip().split()
        fio=new_str[0]+' '+new_str[1]
        subject=new_str[2]
        marks=new_str[3]

        print_dict(add_new_marks(el_jour_dict, fio, subject, marks))
        write_to_el_jour(el_jour_dict)

        new_str=input('введите ФАМИЛИЮ ИМЯ ученика, ПРЕДМЕТ и оценку или СТОП ')

main()
