"====================Строки===================="
# строки - неизменяемый тип данных, который предназначен для хранения текста (символов), заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'не правильная строка"
# SyntaxError: unterminated string literal (detected at line 6)

string4 = "Don't" # внутри двойной кавычки все одинарные это просто символы
string5 = ' "AI Academy" ' # внутри одинарныx кавычек все двоные это просто символы

# '' - Э 
# "" Shift + Э
string6 = """
многострочный текст 
в двойных кавчках
Тут можно ставить "любые" 'кавычки'
"""
string6 = '''
многострочный текст 
в одинарных кавчках
Тут можно ставить "любые" 'кавычки'
'''
# конкатенация
string7 = 'hello' + ' ' +'world'

string1 = 'new'
string2 = 'old'
string1 = string1 + ' '
string3 = string2 + ' hello'
print(string3 + 'world' + string1 + string2)

string4 = 'A '
string4 = string4 * 4
print(string4)

"===================Экранизация строк==================="
# '\n' - перенос на новую строку
print("hello\nworld")

# '\t' - табуляция
print("hello\tworld")

'\'' # отображение '
"\"" # отображение "
print(' Don\'t ')
print(" Don\"t \' \'\"\"\" ! \" \\")

print("\\ \t hello")

print("hello\vworld\vai\vacademy")
print("hello  world\rbyebye")

"==================Методы строк=================="
# методы - функции, которые относятся к определенному классу (типу данных), к ним обращаемся через точку

'hello'.upper() # HELLO
'HELLO'.lower() # hello

'Hello'.swapcase() # hELLO
'hello world'.title() # Hello World
print('hello world'.capitalize()) #Hello world

'hello world'.count('l') # 3
'hello world'.count('ll') # 1
'hello world'.count('ai academy') # 0
'hello world ai academy ai academy'.count('ai academy') # 2

'hello world'.startswith('he') # True
'hello world'.startswith('world') # False
'hello world'.endswith('world') # True

print('hello worlD'.isupper()) # False
print('HELLO WORLD'.isupper()) # True

print('hello worlD'.islower()) # False
print('1234'.isdigit()) # True
print('1234a'.isdigit()) # False
print('hello'.isalpha()) # True
print('hello1'.isalpha()) # False

print('hello   world'.split()) # ['hello', 'world']

print('hello!world'.split('!!!')) # ['hello!world']
print('hello!world'.split('wo')) # ['hello!', 'rld']

'-'.join(['hello', 'world']) # 'hello-world'
''.join(['hello', 'world']) # 'helloworld'
print('!'.join(['hello', 'world', 'ai', 'academy'])) # 'hello!world!ai!academy'
# func()

# print(dir(112))
# dir - показывает все методы и аттрибуты класса (типа данных)
# 1 + 1
# 1.__add__(1)

"==================Индексы=================="
# индекс - порядковый номер элемента в последовательности (символа в строке) (индексация начинается с 0)

'hello world'
# 'h e l l 0   w o r l d'
#  0 1 2 3 4 5 6 7 8 9 10
#                ...-2 -1

string1 = 'hello world'
string1[10] # d
# string1[101] # IndexError
string1[5] # ' '
string1[-1] # 'd'
# string1[-12] # IndexError

# срезы - подстрока (конец не включительно)
string1[2:5] # llo
string1[5:] #  world
string1[:5] # hell
string1[5:11] #  world
string1[:] # hello world

string1[::2] # hlowrd

# variable[start:end:step]

string1[1:-1] # ello worl
string1[-5:-1] # worl
string1[1:5:2] # 'el'
string1[::1] # hello world
string1[::3] # hlwl
string1[::-1] # dlrow olleh
string1[::-2] # drwolh
string1[:-1]
string1[:-1:-2] # ''
# stard - d, stop - d 
# string1 = string1[:-1]
# string1[::-2]
# lo le

# 'h e l l 0   w o r l d'
#  0 1 2 3 4 5 6 7 8 9 10
#                ...-2 -1


"=================Форматирование строк================="
title = 'Iphone 11'
price = 200

format1 = f"Название: {title}\nЦена: {price}"
print(format1)

format2 = "Название: {}\nЦена: {}"
print(format2.format('Картошка', 15))

format2 = "Название: {title}\nЦена: {price}"
print(format2)
print(format2.format(price=15, title='Картошка'))

format3 = "Название: %s\nЦена: %s"
print(format3 % ('Хлеб', 10))

# date 
days = int(input('day: '))
month = int(input('month: '))
year = int(input('year: '))
if days > 31:
    print("дни не могут быть больше 31")
if days > 31:
    print("дни не могут быть больше 31")

date = f"{days}:{month}:{year}"
