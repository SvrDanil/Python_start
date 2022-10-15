#4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random
N= int(input("Введите N "))
list_rnd=[]
arr = []
for i in range(1, N+1):
    list_rnd.append(random.randint(-N, N))
value=1
compared_list=[]
with open('file.txt','r') as file:
    for line in file :
        if -len(list_rnd) <=int(line) <len(list_rnd):
            value*=list_rnd[int(line)]
            compared_list.append(list_rnd[int(line)])
print('Лист совпадений: ', compared_list)
print('Проиведение = ' , value if value !=0  else 'Нет значений')