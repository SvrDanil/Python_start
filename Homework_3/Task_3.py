#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
num_list = [1.1, 1.2, 3.1, 5, 10.01]
max_num, min_num =round(num_list[0] % 1 , 2), round(num_list[1] % 1 ,2)
for i in num_list:
    temp = round(i % 1, 2)
    if max_num < temp:
        max_num = temp
    elif min_num > temp:
        min_num=temp
print(num_list)
print(max_num-min_num)