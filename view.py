

def main_menu():
    print('\nВыберите пункт меню: ')
    print('1. Показать телефонную книгу ')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu()

def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода, некорректные данные!')

def print_phone_book(phone_book: list):
    if len(phone_book)>0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена.')

def print_no_book():
    print('Телефонная книга пуста или не загружена.')

def log_off():
    print('До свидания!')

def load_success():
    print('Телефонная книга загружена')

def save_success():
    print('Телефонная книга сохранена')

def remove_success():
    print('Контакт удален. Не забудьте сохранить внесенные изменения.')

def add_success():
    print('Контакт добавлен. Не забудьте сохранить внесенные изменения.')

def change_success():
    print('Контакт изменен. Не забудьте сохранить внесенные изменения.')

def search_results(list):
    print('Ниже найденные по запросу контакты:')
    if len(list)>0:
        for contact in list:
            print(*contact)
    else:
        print('Поиск не дал результатов.')

def input_new_contact():
    name=input('Введите имя контакта: ')
    phone=input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]

def input_change_contact():
    id=int(input('Введите id контакта, который хотите изменить: '))
    return id

def input_remove_contact():
    id=int(input('Введите id контакта, который хотите удалить: '))
    return id

def search_contact():
    line=input('Введите поисковой запрос: ')
    return line

def change_confirmation(contact: list):
    print(f'Контакт {contact} открыт для редактирования.')
    print(f'Для изменения введите новые данные в консоль. Для продолжения без изменений нажмите enter.')

def get_titles():
    titles=['имя','номер','комментарий']
    return titles
