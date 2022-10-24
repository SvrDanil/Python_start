# Вычислить число c заданной точностью d
from decimal import Decimal
num = input("Ввелите число ")
degree = input("Введите степень округления ")

print(f"Число = {num}")
print(f"Степень = {degree}")

number = Decimal(num)
number = number.quantize(Decimal(degree))
print(f"Число после округления = {number}")
