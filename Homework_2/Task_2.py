#2 –Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N= int(input("Введите N "))
result=[1]
for i in range (1,N+1):
    result.append(i*result[i-1])
print(result[1:])