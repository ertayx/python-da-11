"=============Функции============="
# функция - именованный блок кода, который выполняет определенную задачу и который можно вызвать несколько раз

def coffee_machine(ingredients):
    print(f"кофе с {ingredients}")

coffee_machine("молоком")
# кофе с молоком
coffee_machine("сливками")
# кофе с сливками

def my_sum(x, y):
    return x + y
    print("hello")
    
print(my_sum(1,3))
print(my_sum(2,5)) # 7 


def my_len(obj):
    count = 0
    for i in obj:
        count = count + 1
    print(count)

# 1 iteration - i = 'a' count = 0+1
# 2 iteration - i = 'b' count = 1+1
# 3 iteration - i = 'c' count = 2+1

obj = [1,2,3,4, [1,2]]
my_len(["a", "b", "c"]) # 3
my_len("hello") # 5

obj = "hello"
count = 0
for i in obj:
    # count+=1
    count = count + 1
print(count)

obj = [1,2,3,4,5,6,7]
count = 0
for i in obj:
    # count+=1
    count = count + 1
print(count)

# DRY - dont repeat yourself (не повторяться)

"================Параметры и аргументы================"
# параметры - переменные внутри функции, значение которых мы задаем при вызаове функции (те переменные, которые мы пишем в круглых скобках при создании функции)
# аргументы - значение, которые мы задаем при вызове функции (в параметры)

def my_sum(x, y): # x & y - параметры
    y = 5
    return x + y
print(my_sum(1, 2)) # 6

"=================Виды параметров================="
# 1. обязательные параметры
# 2. не обязательные параметры
# 2.1 с дефолтом (со значением по умолчанию)
# 2.2 *args
# 2.3 **kwargs

def my_sum(x, y=5): # x - обяз, y - не обяз с дефолтом
    return x + y
print(my_sum(1)) # 6
print(my_sum(1, 2)) # 3

def my_sum(x=4, y=5):
    return x + y
print(my_sum(1, 3)) # 8

def my_sub(x, y): 
    return x - y
# print(my_sub()) # TypeError: my_sub() missing 2 required positional arguments: 'x' and 'y'

def my_sum(x=1,y=1): # не обязательные параметры с значениями по умолчанию
    return x+y
print(my_sum())
def cook_burger(meat, cheese='чеддер'):
    burger = f"бургер с {meat} и сыр {cheese}"
    return burger

print(cook_burger('говдиной'))
print(cook_burger('курицей', 'пикарино'))

# def - создаем функцию
# аргументы - передаем данные
# return - возвращаем данные
# вызов - запуск функции

def test():
    return 5

a = test()
print(a)

a = [1,2,3,4]
r = a.pop(0)
print(r) # 1

def pop(new_list, index):
    popped = new_list[index]
    del new_list[index]
    return popped
a = [1,2,3,4]
popped = pop(a, 0)
print(a, '107')
print(popped, '108')

# print - выводит в терминал данные 
# return - возвращает результат функции

def my_sum(x, y):
    return x+y
res = my_sum(1,2)
print(res) # 3

def func(a, b):
    return a**b + 8
    # return None
res = func(1,2)
res

# если мы не пишем return по умолчанию функция вернет None

"==============Виды аргументов=============="
# позиционные (по позиции)
# именованные (по названию (параметр=значение))

def my_sum(x, y):
    return x+y

my_sum(1,2) # x = 1, y = 2 - позиционные аргументы
my_sum(y=3,x=6) # 9 x = 6, y = 3 - именованные аргументы

def cook_burger(meat, cheese='чеддер'):
    burger = f"бургер с {meat} и сыр {cheese}"
    return burger
cook_burger(cheese='говядина', meat='чеддер') # бургер с чеддер и сыр говядина
# cook_burger(cheese='говядина') # TypeError

def func(a,b,c=1):
    return (a*b)-c

func(1, c=2, b=3) # 1
func(1, b=4, c=2) # 2
# func(c=2, 1, b=3) # SyntaxError
# func(1,a=2, b=3) # TypeError
# func(a=1, a=2, b=3) # SyntaxError
# func(b=2, a=1, c=3) # SyntaxError

# new_func()

# def new_func():
#     return 

"==============Распаковка=============="
# *
list1 = list(range(1,11))
list2 = [list1] # [[1,2,3,4,5,6,7,8,9,10]]
list2 = [*list1] # [1,2,3,4,5,6,7,8,9,10]

# **
dict1 = {"a": 5, "b": 6, "c": 7}
# dict2 = {dict1} # {{"a": 5, "b": 6, "c": 7}}
dict2 = {**dict1} # {"a": 5, "b": 6, "c": 7}
list3 = [dict1] # [{"a": 5, "b": 6, "c": 7}]
list3 = [*dict1] # ["a", "b", "c"]

def func(a, b, *args, **kwargs):
    print('a - ', a)
    print('b - ', b)
    print('args - ', args)
    print('kwargs - ', kwargs)

func(1,2, 1,2,3,4, p='c', h='y', u=7)

def func(a,b,c):
    return a+b-c

dict1 = {"a": 1, "b": 2, "c": 3}
print(func(**dict1)) # 0
# func(a=1,b=2,c=3)
# keyword arguments(kwargs) - именованные
# arguments(args) - позиционные

def func(a,b,c, *args):
    # a - 1
    # b - 2
    # c - 3
    return c+a-b
list1 = (1,2,3,2,3,5)
print(func(*list1)) # 2
# func(1,2,3)

print(*'hello')
print([1,2,3]) # [1,2,3]
print(*[1,2,3]) # 1 2 3
print(*(1,2,3)) # 1 2 3
print({"a":5, "b":6}) # {"a":5, "b":6}
test_dict = {"a":5, "b":6}
print(*test_dict) # "a" "b"
{**test_dict}
print({**test_dict}) # {"a":5, "b":6}
# print(**test_dict) # TypeError

print('asdf', 'asdf', sep='_')

a = {"sep": '!'}
print(1,2,3,4, **a) # 1!2!3!4


# print(**test_dict, sep='*')
# print(a=5, b=6, sep='*')
# print(sepe='*')

# документация
def cook_burger(meat:str, cheese):
    """готовит бургер и возвращет его"""

cook_burger(1, 'asdf')
print(1,2,3)

# вызовы других функций внутри функции
def my_stepen(x, y):
    # x = 1
    # y = 2
    return x**y
def my_div_ost(x, y):
    # x = 3
    # y = 1
    return x % y
def my_pow(base:int, exp:int, mod:int) -> int: 
    """кастомный pow"""
    # base = 1
    # exp = 2
    # mod = 3
    stepen = my_stepen(base, exp)
    # stepen = 1
    return my_div_ost(stepen, mod)

print(my_pow(mod=1,base=2,exp=3))

# def my_pow(base, exp, mod):
#     stepen = base ** exp
#     return stepen % mod

"============lambda functions============"

def sum(a, b):
    return a + b
sum(1,2) # 3

sum_lambda = lambda a, b: a + b
sum_lambda(6, 4) # 10

a = [3,1,4,5,2]
a.sort()
print(a)

a = [('Umka', 17), ('Nikita', 64), ('Ascar', 22)]

def get_age(person):
    if person[1] == 17:
        return 100
    return person[1]
a.sort(key=lambda person: person[1] if person[1] != 17 else 100)
# a.sort(key=get_age)
print(a)

# lambda параметры: возвращаемое выражение