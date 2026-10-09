"================Числа================"
# integer (int) - целые числа

a = 5
print(type(a)) # <class 'int'>
print(type(print)) # <class 'builtin_function_or_method'>

a = '10'
print(type(a))
a = int(a)
print(type(a))

a = '10a'
# a = int(a) 
# print(type(a))
# ValueError: invalid literal for int() with base 10: '10a'

# float - числовой тип данных с плавающей точкой (десятичные)
a = '5.23432'

a = float(a)
print(type(a))

print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1) # 0.99999999999
print(0.1+0.1+0.1) # 0.30000000004


# decimal - точное вещественное число
from decimal import Decimal
a = Decimal('0.1') # передавать числа в кавычках
print(a+a+a)
print(a+a+a+a+a+a+a+a+a+a)


"======================Операции над числами======================"
a = 15
b = 3
a + b # сложение
a - b # вычитание
a * b # умножение
a / b # 5.0 деление
a // b # 5 целочисленное деление
a % b # 0 
3 % 2 # 1 остаток от деления
2 ** 3 # 8 возведение в степень
25 ** 0.5 # 5 нахождение кв корня числа

# модуль числа - из отрицательного числа получаем положительное
abs(-5) # 5
abs(10) # 10
abs(-0.1) # 0.1

a = 5
a = a - 3
print(a)

# round - округление числа
print(round(5.6)) # 6
print(round(5.4)) # 5
print(round(5.5)) # 6 (округление в большую сторону)
print(round(5.49, 1)) # 5.5

print(round(10.04565, 3)) # 10.046

from math import sqrt

print(sqrt(25)) # 5

from math import pi
print(pi)

# 1. возводит число в степень
# 2. находит остаток от деления на 3 число
print(pow(2, 3)) # 2 ** 3
print(pow(2, 3, 3)) # 2 ** 3 % 3 == 2

# divmod - функция которая возвращает 2 числа, где 1 - целая часть от деления, 2 - остаток от деления
print(divmod(5, 2)) # (2, 1)
# 5 // 2 = 2
# 5 % 2 = 1