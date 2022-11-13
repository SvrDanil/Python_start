#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности
lst =[1, 2, 3, 5, 1, 5, 3, 10]
lst_unique, lst_reps = [], []
for i in set(lst):
    if lst.count(i) > 1:
        lst_reps.append(i)
    else:
        lst_unique.append(i)
print (f'Начальный список {lst}')
print (f'Только уникальные {lst_unique}')
print (f'Дубликаты {lst_reps}')
print (f'Без повторений {list(set(lst))}')