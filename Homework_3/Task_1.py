#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random
N=int(input("Введите размер списка "))
sum=0
numbers=[]
for i in range(1, N+1):
    numbers.append(random.randint(0, 20))
for index,i in enumerate(numbers):
    print(i)
    if index % 2 != 0 :
        sum = sum + i
print("Сумма = ",sum)
