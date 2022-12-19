import view
import phone_book as pb
import data_base as db



def main_menu(choice: int):
    match choice:
        case 1:
            phone_book=pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2:
            db.load_data_base()
            view.load_success()
        case 3:
            try:
                db.save_data_base()
                view.save_success()
            except:
                view.print_no_book()
        case 4:
            contact=view.input_new_contact()
            pb.add_contact(contact)
            view.add_success()
        case 5:
            phone_book = pb.get_phone_book()
            if phone_book==[]:
                view.print_no_book()
            else:
                view.print_phone_book(phone_book)
                id = view.input_change_contact()
                if pb.change_contact(id) == True:
                    view.change_success()
        case 6:
            try:
                phone_book = pb.get_phone_book()
                view.print_phone_book(phone_book)
                id=view.input_remove_contact()
                if pb.remove_contact(id):
                    view.remove_success()
            except:
                view.print_no_book()
        case 7:
            try:
                phone_book = pb.get_phone_book()
                if phone_book==[]:
                    view.print_phone_book(phone_book)
                else:
                    text=view.search_contact()
                    result=pb.find_contact(text, phone_book)
                    view.search_results(result)
            except:
                view.print_no_book()
        case 0:
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break
