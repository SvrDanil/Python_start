X = bool(input('Введите X '))
Y = bool(input('Введите Y '))
Z = bool(input('Введите Z '))
if not(X or Y or Z) ==  (not X and not Y and not Z):
    print("true")
else :
    print("false")   