from datetime import datetime

def LOG(func):
    def wrapper(*args):
        func(*args)
        with open('log.csv','a',encoding = 'utf-8')as log :
            log.write(f'Была использвана функция {func.__name__}{datetime.now()}\n')
    return wrapper
