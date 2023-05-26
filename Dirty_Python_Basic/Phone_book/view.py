import text_fields as tf


def input_choice(size :int, message: str):
    while True:
        number=input(tf.input_choice)
        if number.isdigit() and 0<int(number)< size+1:
            return int(number)
        else:
            print(tf.wrong_choice(size+1))

def main_menu() -> int:
    print(*tf.menu, sep='\n')
    return input_choice(len(tf.menu)-1, tf.input_choice)


def show_contact(book: list[dict[str, str]], message: str):
    if book:
        print('\n'+'='*72)
        for i, contact in enumerate(book, 1):
             print(f'{i:<3} | {contact["name"]:<20} | {contact["phone"]:<20} | {contact["comment"]:<20}')
        print('='*72,'\n')
    else:
        print(message)

def print_message(message: str):
    print('\n'+'='*72)
    print(message)
    print('='*72 +'\n')


def input_contact(message : list[str]) -> dict[str, str]:
    contact={}
    name = input(message[0])
    phone=input(message[1])
    comment=input(message[2])
    if name: 
        contact['name']=name
    if phone: 
        contact['phone']=phone
    if comment: 
        contact['comment']=comment
    return {'name': name, 'phone': phone, 'comment': comment}

