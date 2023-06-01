import view
import model
import text
#делаем функцию старт

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
               
                view.print_message(text.save_successful)
            case 3:
                #print(model.phone_book)
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                pb = model.get_pb()
                info = view.input_find_contact()
                your_contact = model.find_contact(pb, info, text.find_contact_error)
                view.print_contact(your_contact, text.find_contact_error)

            case 6:
                pb = model.get_pb()
                name = view.input_contact(text.new_contact, text.cancel_input)
                find_index = view.input_index(text.index_change_contact, pb, text.load_error)
                model.change_contact(find_index, name)
                
                pass
            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break