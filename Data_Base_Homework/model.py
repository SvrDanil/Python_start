import csv
def create_database():
    header = ("id","name","surname","birthdate","phone_number")
    with open("data.csv","w") as file:
        writer = csv.writer(file,delimiter = " " )
        writer.writerow (header)
    

def del_row(number):
    try:
        f = open('data.csv')
        f.close()
    except FileNotFoundError:
        print('Файл не существует!')
    with open("data.csv", "r") as file:
        lines = file.readlines()
    del lines[number *2 ]
    del lines[number *2 - 1]
    with open("data.csv", "w") as file:
        file.writelines(lines)
    

def add_row(id,name,surname,birthdate,phone_number):
    try:
        f = open('data.csv')
        f.close()
    except FileNotFoundError:
        print('Файл не существует!')
    with open("data.csv", "a") as file:
        writer = csv.writer(file,delimiter = " " )
        writer.writerow([id, name, surname, birthdate, phone_number])
   
def printout():
    with open("data.csv","r") as file:
        for row in file:
            print(row)

def copy_to_backup():
    file = open("data.csv", "r")
    backup = open("data_backup.csv", "w")
    for line in file:
        backup.write(line)

def back_up_to_file():
    backup = open("data_backup.csv", "r")
    file = open("data.csv", "w")
    for line in backup:
        file.write(line)

def fill_database():
    with open("data.csv", "a") as file:
        writer = csv.writer(file,delimiter = " " )
        writer.writerow([1, "Egor", "Ivanov", "10.12.1995", 4514132])
        writer.writerow([28, "Evgeniy", "Serikov", "15.05.1986", 5146464321])
        writer.writerow([37, "Anton", "Surikov", "11.11.2000", 434564321])
        writer.writerow([11, "Pavel", "Smirnov", "21.08.1964", 1315616163])
        writer.writerow([16, "Igor", "Efremov", "13.01.2001", 5131315614])
        writer.writerow([99, "Danil", "Petrov", "21.05.1991", 35135616])
        writer.writerow([22, "Vlad", "Pavlov", "3.03.2003", 231561456316])






