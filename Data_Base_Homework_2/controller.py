import model
import view

def start():
    connector(view.menu())

def connector(number):
    if number == 1:
         model.create_database()
    elif number == 2:
        model.fill_database()
    elif number == 3:
        model.add_row(view.new_id(),view.new_name(),view.new_surename(),view.new_birthdate(),view.new_number())
    elif number == 4:
        model.del_row(view.minus_row())
    elif number == 5:
        model.printout()
    elif number == 6:
        model.copy_to_backup()
    elif number == 7:
        model.back_up_to_file()
    elif number == 0:
        model.exit()
    else: 
        print("Не верный ввод")
