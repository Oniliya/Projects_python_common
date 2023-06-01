import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        
    
def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book :
        print('\n' + '='*111)
        for contact in book:
            print(f'{contact.get("id"):>3}. {contact.get("name"):<30} | {contact.get("phone"):^30} | {contact.get("comment"):<30}')
        print('='*111 + '\n')
    else:
        print_message(error)

def input_contact(message: str) -> dict[str, str]:
    new= {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key]= value
    return new


def input_search(message :str) -> str :
    return input(message)

# def check_id(id_str) -> int:
#     while True:
#         choise = input(text.input_delete) 
#         if choise.isdigit() and 0<int(choise):
#             return int(choise)
    

