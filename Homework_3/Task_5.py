#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
number = int(input("Введите кол-во элементов "))
fibonacci = []
minus_fibonacci=[]
for i in range (number + 1):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else :
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
for i in range(number, 0, -1):
            minus_fibonacci.append(((-1) ** (i + 1)) * fibonacci[i])
print("Для K = ", number, end ='-->' )
print(minus_fibonacci + fibonacci)         