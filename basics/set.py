"==================Set=================="
# множество - изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных, предназначенный для хранения уникальных значенеий, множества могут хранить в себе только НЕИЗМЕНЯЕМЫЕ типы данных

set1 = {1,2,3,3,4,1,1,1,1,1,1,1}
print(set1) # {1,2,3,4}
set1 = {1}
print(type(set1)) # <class 'set'>
set2 = {True, False, 1, 0}
print(set2) # {False, True}

set2 = {1, 0, True, False}
print(set2) # {0, 1}

"================Методы set================"
# print(dir(set))
# add - добавляет элемент в set
set1 = {1,2,3}
set1.add(1)
set1.add(4)
print(set1)
# {1,2,3,4}

# pop - удаляет значение по принципу FIFO
set1 = {1,2,3,4, 1, 1} # FIFO - first in first out
set1.add(5)
popped = set1.pop()
# set1.pop()
print(set1, popped)


set2 = {"hello", "bambam", "bimbim"}
set2.add("bambam2")
print(set2)
# set2.pop()
# set2.pop()
print(set2)

# remove - удаляет элемент по значению
set3 = {1,2,3}
set3.remove(2)
print(set3) # {1,3}

# difference - отличие первого множества от второго
set1 = {1,2,3}
set2 = {3,4,5}
diff1 = set1.difference(set2) # {1,2}
diff2 = set2.difference(set1) # {4,5}
diff1.union(diff2)
{1,2,4,5}

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.symmetric_difference(set2)) # {1,2,4,5}

print(dir(set1))
print(set1.union(set2))

# intersection
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1.intersection(set2))

set1 = {"math", "english", "french"}
set2 = {"math", "CS", "PE", "sing"}
print(set1.intersection(set2))

# найти пересекающиеся методы list set
# найти отличие методов list от dict
# найти отличие всех методов tuple от list

# узнать применения операторов (-, &, |, ^)

set2 = {"hello", "bambam", "bimbim"}
set2.add("bambam2")
print(set2)

set2 = {"1", "2", "3"}
set2.add("4")
print(set2)


set1 = {1,2,3}
set2 = {3,4,5}
print(set1|set2)