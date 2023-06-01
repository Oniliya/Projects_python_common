import view
import model
import text


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1: # 1. Открыть файл
                model.open_pb()
                view.print_message(text.load_successfull)

            case 2: # 2. Сохранить файл
                model.save_pb()
                view.print_message(text.save_successfull)

            case 3: # 3. Показать контакты
                pb = model.get_pb()
                view.print_contacts(pb, text.pb_empty)

            case 4: # 4. Добавить контакт
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successfull(name))

            case 5: # 5. Найти контакт
                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))


            case 6: # 6. Изменить контакт
                key_word = view.input_search(text.input_change)
                result = model.search_contact(key_word)
                if result:

                    if len(result) != 1:
                        view.print_contacts(result, text.contact_not_found)
                        current_id = view.input_search(text.input_index)

                    else:      
                        current_id=result[0].get('id')

                    new_contact = view.input_contact(text.change_contact)     
                    name = model.change_contact(new_contact, current_id)   
                    view.print_message(text.change_successfull(name))
                else:
                    view.print_message(text.empty_search(key_word))


            case 7: # 7. Удалить контакт
                key_word = view.input_search(text.input_delete)  
                if model.find_id(int(key_word)):
                    print(model.find_id(int(key_word)))
                    model.delete_contact(int(key_word))
                    view.print_message(text.delete_contact)
                else:
                    view.print_message(text.delete_none)

            case 8: # 8. Выход
                break
