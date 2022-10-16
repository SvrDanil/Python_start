#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number= str(input("Введите число "))
number = number.replace('.', '')
number_list= list (number)
number_whole=map(int,number_list)
s=sum(number_whole)
print(s)

