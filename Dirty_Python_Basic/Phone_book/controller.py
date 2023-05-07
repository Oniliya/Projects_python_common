import text_fields as tf
import view
import model

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(tf.open_successful)
            case 2:
                pass
            case 3:
                pb = model.phone_book
                view.show_contact(pb, tf.no_phone_book)
            case 4:
                new_contact = view.input_contact(tf.new_contact)

                model.add_contact(new_contact)
                view.print_message(tf.add_successful)
            case 5:
                pass
            case 6:
                pb=model.phone_book
                view.show_contact(pb,'')
                choise = view.input_choice(len(pb), tf.change_choice-1)
                change_contact=view.input_contact(tf.change_contact)
                res = model.change(choise, change_contact)
                view.print_message(tf.changed(res['name']))
            case 7:
                pass
            case 8:
                pass
