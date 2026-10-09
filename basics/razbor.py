# list dict set

# int float tuple str bool nonetype frozenset

var = 1234


def even_numbers(list_):
    new_list = []
    for i in list_:
        if i % 2 ==0:
            new_list.append(i)
    return new_list

# DRY - dont repeat yourself
a = [2000, 20001, 200034]
b = [1,2,3,4]
even_numbers(a)
even_numbers(b)
# print
# input
# dir
# type
# int
# str
# list

# if
# elif
# else
# if else
# while
# for in 
# break
# continue
# return
# import 
# from

# + - / // % = == != >= <= * **

import math
print(math.sqrt(16))
# print(4**2)
print(pow(4, 2, 3)) # 4**2 % 3 = 1

input

def d():
    print("drive")
def t():
    print("tormoz")

# traffic = input("color")
# if traffic == 'green':
#     d()
# elif traffic == 'red':
#     t()

# a = None
a = ''
# full_name	salary	id	position
# Umka	1000000	123	povar
# Nikita	20000	124	hr
# 	10000000	125	povar
# ertay	1000000	123	povar
a = [{
    "name": "ertay",
    "salary": 999999,
    "id": 125,
    "position": "kura"
},
{
    "name": "umka",
    "salary": 100000,
    "id": 123,
    "position": "povar"
},{
    "name": None,
    "salary": 10000000,
    "id": 124,
    "position": "povar"
}]

a = [{"a": 5}, {"a": 4}, {"a": 3}]

a = 5
b = 5
print(a is b)
print(a == b)

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b) 