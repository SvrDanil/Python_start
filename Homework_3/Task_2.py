#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
N=int(input("Введите размер списка "))
numbers=[]
for i in range(1, N+1):
    numbers.append(random.randint(0, 20))
new_numbers=[]
for j in range ( (N + 1)  // 2):
    mult = numbers[j] * numbers[- j - 1]
    new_numbers.append(mult)
print(numbers)
print(new_numbers)
