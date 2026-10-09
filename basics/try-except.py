"===================Exceptions==================="
# Исключения (ошибки) - обькты, которые прерывают работу кода, если не были обратоны

TypeError 
# Когда пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

# for i in 100000:
#     print(i)

# 5 + 'a'

# def func(a):
#     return 
# func()

SyntaxError
# исключение, которое выходит, когда в коде допущена синтаксическая ошибка

# (
# '
# a = 
# def func(a, b)
#     return a, b
# func(6 7)

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществуещему индексу

# list_ = [1,2,3,4]
# list_[1000]



ValueError
# когда мы передаем в функцию не корректный для нее тип данных
# когда идет не соответсвие количеста обьектов при распаковке

# int('10a')
# a, b = [1,2,3]

KeyError
# выходит когда мы обращаемся по несуществуещему ключу
dict_ = {"name": "Umka"}

# dict_['age']
# dict_.pop('age')

# обработка KeyError
# try:
#     age = dict_['age']
# except KeyError:
#     age = None
# print(age)

NameError
# выходит когда вызываем несуществуещую переменную или же функцию

# umka
# mac
# new_func()
ZeroDivisionError
# при делении на 0

# 5 / 0

AttributeError
# выходит когда мы обращаемся по несуществуещему аттрибуту или методу обьекта 

# [1,2,3].replace(1, 'a')
# a = 1
# a.asdfasdf()

Exception
# исключение которое мы можем создать 

"===============Вызов исключений==============="
# raise NameError
# NameError

# raise NameError('Не правильное имя')
# num = input('ВВЕДИТЕ ЧИСЛО: ')
# if type(num) != type(int):
#     raise ValueError('ну я же попросил число')

# print("after raise")

"=================Обработка исключений================="
# что бы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать вызвонное исключение

# import random
# print("==Guessing Game====")
# print("You need to guess a number from 1 to 100")
# print('You will have 5 attempts and hints as you play')
# print('if your number is + - 15 then Cold')
# print('if + - 10 then Warm, + - 5 hot, + - 2 Almost there!!!')
# print('good Luck!')
# attempts=5
# computers_choose=random.randint(1,100)
# # try:
# while attempts>0:
#     try:
#         players_choose=int(input('Enter the number'))
#     except ValueError:
#         print("type a number")
#         continue
#     attempts=attempts-1
#     #break rule
#     if computers_choose==players_choose:
#         print("Great Job you WIN")
#         break
#     #hints
#     if abs(computers_choose-players_choose)>=15:
#         print('Cold')
#     elif abs(computers_choose-players_choose)>=10:
#         print('Warm')
#     elif abs(computers_choose-players_choose)>=5:
#         print('Hot')
#     elif abs(computers_choose-players_choose)>=2:
#         print('Almost there!!!')
#     else:
#         print('Pay attention')

# print('==Game Over====')
# print(f'the secret number was {computers_choose}')

# try:
#     body
# except Exception:
#     body2
# else:
#     body if there is no exceptions
# finally:
#     body which work always

# try:
#     num = int(input('ВВЕДИТЕ ЧИСЛО: '))
#     num + 'a'
# except ValueError:
#     print("введите число, не выпендривайтесь)")
# except TypeError:
#     print("введите число, не выпендривайтесь)")
# else:
#     print("введенное число: ", num)
# finally:
#     print("До свидания")

# try: 
#     # код, который возможно вызовет ошибку
#     a = int(input())
#     b = int(input())
#     res = a // b
#     list_ = [1,2,3,4]
#     list_[res]
# except ZeroDivisionError:
#     # код, который отработает только если возникла ZeroDivisionError
#     print('число не должно равнятся 0')
# except ValueError:
#     # код, который отработает только если возникла ValueError
#     print('введите число')
# except Exception as error:
#     # код, который отработает только если возникла любая ошибка кроме ValueError и ZeroDivisionError 
#     print(error)
# else:
#     # код, который отработает если нет никаких ошибок
#     print(res, 'else')
# finally:
#     # код, который будет работать в любом случае
#     print("bye")


def func():
    try:
        return 1
    finally:
        print('hello')

# 1 
# 0 

var = func()
print(var)