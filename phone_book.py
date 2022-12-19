phone_book=[]
import view


def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book=new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name=phone_book[id-1][0]
    confirm=input(f'Вы действительно хотите удалить контакт {name}? (y/n): ')
    if confirm.lower()=='y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id):
    global phone_book
    con=phone_book[id-1]
    view.change_confirmation(con)
    flag=False
    for i in range(len(con)):
        print(view.get_titles()[i])
        print(con[i])
        change=input()
        if change!='':
            phone_book[id-1][i]=change
            flag=True
    return flag

def find_contact(text, phone_book):
    results=[]
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if text.lower() in phone_book[i][j].lower():
                results.append(phone_book[i])
                break
    return results
