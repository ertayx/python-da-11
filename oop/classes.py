"====================OOP===================="
# OOP - object-oriented programming
# ООП - обьектно ориентированное программирование (парадигма)

# class Student()

student1_name = "umka"
student1_age = 17
student1_group = "analytics 11"
student1_legs = 2

student2_name = "nikita"
student2_age = 19
student2_group = "analytics 10"
student2_legs = 2


class Student: # класс - шаблон
    legs = 2 # аттрибуты - переменные внутри класса
    arms = 2
    # name = 'umka'

    # функция внутри класса это метод
    def __init__(self, name, age, group):
        # __init__ - метод, который будет добавлять в обьект те аттрибуты, которые отличаются у разных обьектов
        # self - ссылка на обьект (который только что создался)
        self.name = name
        self.age = age
        self.group = group

    # функция внутри класса это метод
    def study(self, mentor):
        print("учусь в группе", self.group)
        print("у ментора по имени", mentor)
    
student1 = Student('umka', 17, 'analytics 11') # обьект от класса Student
student2 = Student('nikita', 19, 'analytics 10')

print(student1.group) # analytics 11
print(student1_group) # analytics 11
print(student1.study('Ertay')) # учусь в группе analytics 11 \n у ментора по имени Ertay
print(student2.study('Sanzhik')) # # учусь в группе analytics 10
print(student1.legs)

print(type(student1)) # <class '__main__.Student'>
print(type(1)) # <class 'int'>

def func():
    return 1 + 1
a = func()
print(type(func)) # <class 'function'>


class Car:
    wheels = 4
    riding_wheel = True

    def __init__(self, name, year, color, engine, serial_number):
        self.name = name
        self.year = year
        self.color = color
        self.engine = engine
        self.serial_number = serial_number

    def drive(self):
        print("woooo drive")

    def stop(self):
        print('stop')

car1 = Car('Mercedes Benz', 2003, 'black', 'M271', 'ADSSG234553')
car2 = Car('Lexus', 2005, 'gold', '2jz', 'ADSSG23412343')
print(car1.drive())
print(car2.drive())
car3 = Car('Mercedes Benz', 2003, 'black', 'M271', 'ADSSG234553')
car4 = Car('Mercedes Benz', 2003, 'black', 'M271', 'ADSSG234553')

class Sniper:
    health = 100

    def __init__(self, name):
        self.name = name

    def shoot(self, sniper2):
        sniper2.health -= 20
        print('атаковал', self)
        print(f'у {sniper2} осталось {sniper2.health}')

    def __str__(self):
        return self.name

sniper1 = Sniper('1')
sniper2 = Sniper('2')

sniper1.shoot(sniper2)
sniper1.shoot(sniper2)

1+1

# НАСЛЕДОВАНИЕ
# ПОЛИМОРФИЗМ
# ИНКАПСУЛЯЦИЯ
# АБСТРАКЦИЯ
# АССОЦИАЦИЯ

# SOLID

class BankAccount:
    balance = 0

    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email

    def popolnenye(self, amount):
        self.balance += amount

    def send(self, reciever, amount):
        self.balance -= amount
        reciever.balance += amount

umka = BankAccount('umka', 'password', 'umka@gmail.com')
nikita = BankAccount('nikita', 'password', 'nikita@gmail.com')

umka.popolnenye(20000)
print(umka.balance, 'umka balance')
umka.send(nikita, 1000)
print(umka.balance, 'umka balance')
print(nikita.balance, 'nikita balance')