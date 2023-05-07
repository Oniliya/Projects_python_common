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

import string

def create_dict(subject: str, name: dict[fio: str, grade: list])-> dict:
    my_dict={}
    #     if Variables.BOT_DICT.get(message.from_user.first_name, None):
    #     Variables.BOT_DICT[message.from_user.first_name] += 1
    # else:
    #     Variables.BOT_DICT[message.from_user.first_name] = 1
    if my_dict.get(subject, None):
        if my_dict[subject].get(name,None):
            my_dict[subject][name][fio]=grade
    return None

def main():
    with open(PATH, 'w', encoding='UTF-8'):
        pass


main()
