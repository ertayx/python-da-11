"==============Области видимости=============="
# LEGB - local, enclosed, global, built-in

"================Built-in================"
# встроенное пространсво имен (print, input, dir, len)

"==============Global=============="
# все переменные, которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные, можно использовать globals
a = 5
b = 'hello'

def func():
    # a = 5
    a += 5
    name = 'Umka'
    print()

# name
# name = 'Nikita'
print(globals())
# func()
a += 1
# a += 5
# print(a)

"===============Enclosed==============="
# замкнутое пространство имен - локальное пространство, у котого есть внутренне локальное пространство

def func():
    var = 'enclosed'
    def inner_func():
        var = 'local'
        print(var) # local (2)
        # var1 += '1'
    print(var) # enclosed (1)
    inner_func()
    # print(var) # enclosed

# print()
func()
# inner_func() - будет ошибка потому что inner_func находится внутри локального пространства

"===============Local==============="
# локальное пространство имен - переменные, созданные внутри функции

globals()
locals()

def func():
    a = 10
    def inner_func():
        b = 7

    print(locals())
    # print(globals())
    inner_func()
    
func()

# print(globals())
# print(locals())

count = 1
def start_counter():
    global count
    count += 1

start_counter() # 2
start_counter() # 3
start_counter() # 4
print(count)


var = 3
def func():
    var = 4
    def inner_func():
        # global var # 3
        nonlocal var # 4
        var+=1
        print(var) # 5
    inner_func()

func()

# a = 5
# def func():
#     nonlocal a
#     a

# global
def func():
    # enclosed
    var = 2
    def inner_func():
        # enclosed
        nonlocal var
        var = 3
        def inner_inner_func():
            # local
            nonlocal var
            var += 1 
            print(var) # 4
        inner_inner_func()
    inner_func()
func()

# рекурсия


def recursive_func(a):
    print(a)
    if a > 5:
        recursive_func(a-1)

recursive_func(10)