# # 
# открыть файл (txt) не json
# сохранить файл
# распечатеть все что есть
# добавить контакт
# найти контакт
# изменить контакт
# удалить контакт
# выход

from t1_sem8 import PATH, PATH_1

# phone_book=[list[dict[str, str]]]
phone_book=[]

def open_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data=file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        contact = {'name': contact[0].strip(), 'phone':contact[1].strip(), 'comment': contact[2].strip()}
        phone_book.append(contact)
    
    print(phone_book)

def save_file(phone_list :list):
    with open(PATH_1, 'w', encoding='UTF-8') as file:
        for contact in phone_list:
            # print(contact)
            for key, value in contact.items():
                print(value, end=' : ', file=file)
            print(file=file)
            



open_file()

save_file(phone_book)