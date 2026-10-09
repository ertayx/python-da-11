"===================Циклы==================="
# цикл - это блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемыми обьектами, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого обьекта

# while

students = ["Umka", "Nikita", "Tima", "Ertay", 123456, False, None, [1,2,3]]
for st in students:
    print(f"check dz for {st}")
    # print("hello")

# print(f"check dz for {student}")
# print(f"check dz for {student}")
# print(f"check dz for {student}")

for i in range(1, 6):
    if i % 2 == 0:
        print("chet", i)
    else:
        print("ne chet", i)

for a in "hello":
    print(a)

# 1 iteration a = 'h'
# 2 iteration a = 'e'
# 3 iteration a = 'l'
# 4 iteration a = 'l'
# 5 iteration a = 'o'
n = 1
while n <= 10:
    n += 1
    print(n)

battery = 100
counter = 1
while battery > 0:
    print("Убираюсь...", counter)
    battery -= 10
    counter += 1

# while 1 == 1:
#     print("o")

# while условие:
#   тело

# for переменная in итерируемый обьект:
#   тело

# from random import randint

# popytka = 4
# random_num = randint(0, 10)

# while popytka > 0:
#     num = int(input("vvedite chislo: "))
#     # popytka = popytka - 1
#     if num == random_num:
#         print("W")
#         break
#     elif num > random_num:
#         print("lower")
#     elif num < random_num:
#         print("higher")
#     popytka -= 1
#     if popytka == 0:
#         print(f"gameover L, chislo bylo {random_num}")


"==================Ключевые слова в циклах=================="
# break - полностью останавливает работу цикла (выходит из цикла)
# continue - переходит к следующей итерации

for i in range(10):
    print(i)
    # if i == 3:
    break

while 1 == 1:
    print("hello")
    break

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)
    continue
    # continue

list1 = [1, 2, 1, 1, 3, 4, 5, 1]
# 1 = 1
for i in list1:
    print(i)
    if i == 1:
        list1.remove(i)

new_list = []
for i in list1:
    if i != 1:
        new_list.append(i)
print(new_list)

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)


# Ctrl + C - останавливает процесс в терминале