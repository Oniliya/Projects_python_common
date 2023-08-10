import view
import model
import text

def start():
    while True:
        choise = view.main_menu()

        match choise:
            # 1. Открыть файл с заметками
            case 1:
                model.open_nb()
                view.print_message(text.load_successful)

            # 2. Сохранить файл с заметками
            case 2:
                model.save_nb()
                view.print_message(text.save_successful)

            # 3. Показать заметки
            case 3:
                nb = model.get_nb()
                view.print_notes(nb, text.nb_empty)

            # 4. Добавить заметку
            case 4:
                note = view.input_note(text.input_new_note)
                note_head = model.add_note(note)
                view.print_message(text.new_note_successful(note_head))

            # 5. Найти заметку
            case 5:
                key_word = view.input_search(text.input_search)
                result = model.searh_note(key_word)
                view.print_notes(result, text.empty_searсh(key_word))

            # 6. Изменить заметку
            case 6:
                key_word = view.input_search(text.input_change)
                result = model.searh_note(key_word)
                if result:
                    view.print_notes(result, text.empty_searсh(key_word))
                    current_id = view.input_search(text.input_index)
                    new_note = view.input_note(text.change_note)
                    note_head = model.change_note(new_note, current_id)
                    view.print_message(text.change_successful(note_head))

                else:
                    view.print_message(text.empty_searсh(key_word))

            # 7. Удалить заметку
            case 7:
                key_word = view.input_search(text.input_delete)
                result = model.searh_note(key_word)
                if result:
                    view.print_notes(result, text.empty_searсh(key_word))
                    current_id = view.input_search(text.input_index)

                    view.print_message(text.delete_note(current_id))
                    model.delete_note(int(current_id))

                else:
                    view.print_message(text.empty_searсh(key_word))

            # 8. Выход
            case 8:
                break

