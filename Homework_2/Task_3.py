#3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
n= int(input("Введите n "))
list = [(1+1/i)**i for i in range(1, n+1)]
print(f'Сумма: {sum(list)}')
 