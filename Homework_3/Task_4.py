#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input("Ввведите число "))
temp = ''
while number > 0:
    temp = str(number % 2) + temp
    number = number // 2
 
print(temp)