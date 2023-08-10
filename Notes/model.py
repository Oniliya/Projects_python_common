import text
import datetime

note_book: list[dict[str, str]] = []
path = 'notes.csv'


def open_nb():
    global note_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for note in data:
        note = note.strip().split(';')
        new = {'id': note[0], 'note_head': note[1], 'note_body': note[2], 'note_date': note[3]}
        note_book.append(new)


def save_nb():
    global note_book
    data = []
    for note in note_book:
        data.append(f"{note['id']};{note['note_head']};{note['note_body']};{note['note_date']}")

    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_nb():
    global note_book
    return note_book


def add_note(new: dict[str, str]) -> str:
    global note_book
    new_id = int(note_book[-1].get('id')) + 1
    new['id'] = str(new_id)
    note_book.append(new)
    return new.get('note_head')


def searh_note(word: str) -> list[dict[str, str]]:
    global note_book
    result: list[dict[str, str]] = []
    for note in note_book:
        for field in note.values():
            if field.lower().find(word.lower()) != -1:
                result.append(note)
                break
    return result

def change_note(new: dict, index: int) -> str:
    global note_book
    for note in note_book:
        if index == note.get('id'):
            note['note_head'] = new.get('note_head', note.get('note_head'))
            note['note_body'] = new.get('note_body', note.get('note_body'))
            note['note_date'] = str(datetime.date.today())
            return note.get('note_head')


def delete_note(del_id: int):
    global note_book
    temp_book: list[dict[str, str]] = []
    for note in note_book:
        if del_id != int(note.get('id')):
            temp_book.append({'id': note['id'], 'note_head': note['note_head'], 'note_body': note['note_body'],
                              'note_date': note['note_date']})
    note_book = temp_book
