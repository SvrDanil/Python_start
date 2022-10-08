X = int(input('Введите X '))
Y = int(input('Введите Y '))
if X > 0 and Y > 0 :
    print('1 Четверть')
elif X < 0 and Y > 0 :
    print('2 Четверть')
elif X < 0 and Y < 0 :
    print('3 Четверть')
elif X > 0 and Y < 0 : 
    print('4 Четверть')      