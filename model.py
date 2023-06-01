phone_book: list[dict[str, str]] = []
path = 'phone.txt'


#2 открыть файл
def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        #print(data)
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})
            #phone_book.append(contact)
    #print(phone_book)


#3 показать контакт
def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book

#добавить контакт
def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')

#записать контакт
def save_pb():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))

#удалить контакт
def del_contact(index: int):
    return phone_book.pop(index - 1).get('name')

#найти контакт

def find_contact(pb: list[dict[str, str]], message: str, error: str):
    global phone_book, path
    data: list[dict[str, str]] = []
    for contact in phone_book:
        for value in contact.values():
            if message.lower() in value.lower():
                data.append(contact)
                #print(data)
                return data
            else:
                error
   



#изменить контакт
def change_contact(info_contact, dict_contact: dict[str, str], error):
    global phone_book, path
    #print(dict_contact)
    for contact in phone_book:
        for value in contact.values():
            if info_contact.lower() in value.lower():
                contact['name'] = dict_contact.get('name')
                contact['phone'] = dict_contact.get('phone')
                contact['comment'] = dict_contact.get('comment')
            else:
                error
    return phone_book
               