"================Работа с файлами================"
# open - функция, которая открывает файл в определенном режиме
# режимы:
# r - read (только для чтения)
# w - write (только для записи, каждый раз файл очищается)
# a - append (только для дозаписи, добавляет в конец)
# x - создает файл, если такой файл есть выдает ошибку
# b - binary (в бинарном виде)
# посмтореть какие комбинации режимов существуют hw

"====================Read===================="
file = open('files/test.txt', 'r')
# print(dir(file))
print(file.writable()) # False
print(file.readable()) # True
print(file.read()) # ai\nacademy\vcoding\nis easy
print(file.read()) # ''
# каретка |
file.seek(2) # перенос каретки
print(file.read()) # \nacademy\vcoding\nis easy

file.seek(0)
print(file.readlines())
file.seek(0)
print(file.readline()) # ai\nacademy\vcoding\nis easy 
print(file.readline()) # 234
print(file.readline(1)) # a

file.seek(0)
print(file.tell()) # 0
print(file.readline()) 
print(file.tell()) # 30

file.close()

"================Write================"
file = open('files/new_file', 'w')
# если файла нет - создаст его
file.writable() # True
file.readable() # False
file.write('coding is easy\n') # 16
print(file.tell()) # 16
# file.seek(0)
file.write('umka monstr\n')

file.writelines(['Hello\t', 'world\n'])
file.close()

"================Append================"
# добавляет в конец строку
file = open('files/new_file', 'a')
file.write('new_row\n')
file.write('\nUmka moch')
file.close()

# file = open('files/files.py', 'a')
# file.write('\ndef func(a, b)\n')
# file.write('\treturn a, b\n')
# file.write('func(1,2)\n')
# file.close()

file = open('umka.py', '+a')
print(file.writable())
print(file.readable())
file.close()

"===============Контекстный менеджер==============="
try:
    file = open('files/new_file', 'a')
    file.read()
finally:
    file.close()

with open('files/new_file', 'r') as f:
    print(f.read())
    print(f.readlines())

f.read() # Error