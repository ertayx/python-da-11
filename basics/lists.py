"====================List===================="
# списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list1 = [1, 2, 3, 'hello', [2,3, 12,3 ,54,6, 8,9, [1,2,3]], None, True, False]
list1[3]
print(list1[3][-1])
# list1[1][-1]
print(list1[4]) # [2,3]
print(list1[-1]) # False
print(list1[0:3]) # [1, 2, 3]

print(list1[::-1]) # [False, True, None, [2, 3], 'hello', 3, 2, 1]

print(list("hello")) 
# ['h', 'e', 'l', 'l', 'o']

print(list(range(1, 11)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(range(1, 1000001))
# print(a)
list2 = [1]
list2 * 5
print(list2)

"==================Методы списков=================="
# print(dir(list))
# append - добавляет элемент в конец списка

list2 = []
list2.append(1)
list2.append(67)
list2.append([67, None])
print(list2)
# [1, 67, [67, None]]
# list2[:-2] == [1]
# [1, "hello"]
# list3 = list2[:-2].append('hello')
# print(list2)

a = 'asdf'
b = a.upper()
print(a)

# pop - удаляет элемент из списка по индексу
# прочитать что делает pop
list1 = [1,2,3,4]
# [1, 2, 3, 4]
#  0  1  2  3
# -4 -3 -2 -1
list1.pop(-1) # [1, 3, 4]
list1.pop(1) # [1, 4]
# list1.pop(0) # [2]
# list1.pop(0) # []
# # list1.pop() # IndexError
print(list1)

# remove - удаляет элемент из списка по значению
list1 = [1,2,3,4, 'hello']
list1.remove('hello')
print(list1)

# count
list1 = [1,1,2,3,4, 'hello']
print(list1.count(1)) # 2
print(list1)
print(list1.count('1')) # 0
print(list1.count('hello')) # 1

# index
list1 = [1,1,2,3,4, 'hello']
print(list1.index('hello')) # 5

# insert
list1 = [1,1,2,3,4, 'hello']
list1.insert(1, False)
print(list1)
# [1, False, 1, 2, 3, 4, 'hello']
list1.insert(3, [1,2,3])
print(list1)
# [1, False, 1, [1, 2, 3], 2, 3, 4, 'hello']

# extend - hw
list1 = [1,2,3]
list1.extend('hello')
list1.extend([1,2,3])
list1.append([1,2,3])
# [1,2,3,'h','e','l','l','o', 1,2,3, [1,2,3]]

# sort
list1 = [1,1,2,3,4, 1, 2, 0, -12, -67]
list1.sort()
print(list1)
# [-67, -12, 0, 1, 1, 1, 2, 2, 3, 4]

list1 = ['c', 'd', 'b', 'a', 'ab'] 
list1.sort()
print(list1)
# ['a', 'ab', 'b', 'c', 'd']

list1 = ['c', 'd', 'b', 'a', 'A', 'B'] 
list1.sort()
print(list1)
# ['A', 'B', 'a', 'b', 'c', 'd']

list1 = ['c', 'd', 'b', 'a', 'A', 'B'] 
list1.sort(reverse=True)
print(list1)
# ['d', 'c', 'b', 'a', 'B', 'A']

# clear
list1 = ['c', 'd', 'b', 'a', 'A', 'B', [1,2]] 
list1.clear()
print(list1)


print(len(list1))

# list1 = [1,2,3, 'umka', None, [1]]
print('bam' in 'Umkabambam')

a = 5
name = 'ertay'

from decimal import Decimal

bool
float # 10.8 не точный 
Decimal # 10.8 точный
str
None
int # 10

list
print
input

print(0.1+0.1+0.1)
print("hello"[2:5])

# and # i
# or # ili
# not # ne

# 5 == 6 and 6 == 6 # False 
# # True and False - False

# if погода == 'ветренная':
#     print("одеться тепло")
# elif погода == 'солнечная':
#     print("оденься легко")
# else:
#     print("выходим")

# print(list(range(1,11,3)))
print(set(range(1,5,2)))