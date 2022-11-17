

def menu():
    print("1 - создать базу данных")
    print("2 - заполнить базу данных")
    print("3 - добавить строку")
    print("4 - удалить строку")
    print("5 - вывести БД в консоль")
    print("6 - создать backup")
    print("7 - перезаписать из backup")
    return int(input("Введите номер функции : "))

def new_id():
    id = int(input("введите id: "))
    return id

def new_name():
    name = str(input("ведите Имя : "))
    return name

def new_surename():
    surename = str(input("Введите Фамилию : "))
    return surename

def new_birthdate():
    birthdate = str(input("Введите дату рождения : "))
    return  birthdate
    
def new_number():
    number = int(input("Введите номер телефона : "))
    return  number
    
def minus_row():
    return  int(input("Введите номер строки на удаление: "))