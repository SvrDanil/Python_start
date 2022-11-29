import csv
import os
from logger import LOG

@LOG
def create_database():
    header = ("id","name","surname","birthdate","grade")
    with open("data.csv","w",encoding = 'utf-8') as file:
        writer = csv.writer(file,delimiter = " " )
        writer.writerow (header)
    
@LOG
def del_row(number):
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as file:
            lines = file.readlines()
            del lines[number *2 ]
            del lines[number *2 - 1]
        with open("data.csv", "w",encoding = 'utf-8') as file:
            file.writelines(lines)
    else: print("Создайте базу данных")
    
@LOG
def add_row(id,name,surname,birthdate,phone_number):
    if os.path.exists("data.csv"):
        with open("data.csv", "a",encoding = 'utf-8') as file:
            writer = csv.writer(file,delimiter = " ")
            writer.writerow([id, name, surname, birthdate, phone_number])
    else: print("Создайте базу данных")
   

@LOG
def printout():
    if os.path.exists("data.csv"):
        with open("data.csv","r",encoding = 'utf-8') as file:
            for row in file:
                print(row)
    else:print("Создайте базу данных")

@LOG
def copy_to_backup():
    file = open("data.csv", "r",encoding = 'utf-8')
    backup = open("data_backup.csv", "w",encoding = 'utf-8')
    for line in file:
        backup.write(line)

@LOG
def back_up_to_file():
    backup = open("data_backup.csv", "r",encoding = 'utf-8')
    file = open("data.csv", "w",encoding = 'utf-8')
    for line in backup:
        file.write(line)

@LOG
def fill_database():
    if os.path.exists("data.csv"):
        with open("data.csv", "a") as file:
            writer = csv.writer(file,delimiter = " ")
            writer.writerow([1, "Egor", "Ivanov", "10.12.1995", 1])
            writer.writerow([3, "Evgeniy", "Serikov", "15.05.1986", 2])
            writer.writerow([37, "Anton", "Surikov", "11.11.2000", 3])
            writer.writerow([11, "Pavel", "Smirnov", "21.08.1964", 4])
            writer.writerow([16, "Igor", "Efremov", "13.01.2001", 5])
            writer.writerow([15, "Danil", "Petrov", "21.05.1991", 5])
            writer.writerow([22, "Vlad", "Pavlov", "3.03.2003", 6])
    else: print("Создайте базу данных")

@LOG
def exit():
    raise SystemExit




