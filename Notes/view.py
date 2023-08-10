import text
import datetime


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '*' * len(message))
    print(message)
    print('*' * len(message) + '\n')


def print_notes(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '*' * 240)
        for note in book:
            print(
                f'{note.get("id"):>5}. {note.get("note_head"):<50} || {note.get("note_body"):^150} || {note.get("note_date"):>12}')
        print('=' * 240 + '\n')
    else:
        print_message(error)


def input_note(message: str) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_note.items():
        if key != 'note_date':
            value = input(txt)
            if value:
                new[key] = value
        new['note_date'] = str(datetime.date.today())
    return new


def input_search(message: str) -> str:
    return input(message)

