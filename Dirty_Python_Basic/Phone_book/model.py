phone_book=[list[dict[str, str]]]
PATH='phone_book.txt'

def open_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data=file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        contact = {'name': contact[0], 'phone':contact[1], 'comment': contact[2]}
        phone_book.append(contact)


def add_contact(contact :dict[str, str]):
    phone_book.append(contact)


def change(ind:int, contact:dict[str,str])-> dict[str, str]:
    cur_contact= phone_book[ind]
    # name = contact.get('name')
    # phone = contact.get('phone')
    # comment = contact.get('comment')
    # new_contact = {'name':name if name else cur_contact.get('name'),
    #                'phone':phone if phone else cur_contact.get('phone'),
    #                'comment':comment if comment else cur_contact.get('comment'),
    #                    }
    cur_contact.update(contact)
    resalt = phone_book.pop(ind)
    phone_book.insert(ind, cur_contact)
    return resalt