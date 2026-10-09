"===================Словари==================="
# dict - изменяемый, итерируемый, неупорядоченный, неидексируемый тип данных, для хранения данных в парах (ключ:значение) 

dict1 = {
    "name": "Ertay",
    "age": 20,
    "last_name": "Esenbekov"
}
print(dict1["name"])

[
    {
        "id": 1241324,
        "price": 2000000,
        "title": "It",
        "description": "xoroshyi"
    },
    {
        "id": 12,
        "price": 3000000,
        "title": "Koshka",
        "description": "xoroshaya"
    }
]


dict1 = {
    "name": "Umka",
    "name": "Nikita",
    "age": 17,
    "last_name": "Toychubekov",
    "job": {
        "title":"ai academy",
        "salary": 150000,
        "currency": "COM" 
    }
}
# ключами в словаре могут быть только не изменяемые типы данных
# int float str bool nonetype tuple frozenset
print(dict1["name"])
print(dict1["job"]["title"]) # ai academy

# dict1[18] # KeyError
"=================Создание словарей================="
list1 = ["ab", "cd", "ef"]
dict1 = dict(list1)
print(dict1)
# {'a': 'b', 'c': 'd', 'e': 'f'}

list2 = [("name", "Umka"), ("age", 17)]
dict2 = dict(list2)
print(dict2)

dict2["name"] = "nikita"
dict2["last_name"] = "grebnev"
print(dict2["name"])
# var = {key:value, key: value}

a = {
    1: [1, 23]
}
print(a[1])

print(type(a))
"===================Методы словарей==================="
print(dir(a))

e211 = {
    "car_name": "Mersedes Benz",
    "price": 20000000,
    "model": "W211",
    "class": "E",
    "year": 2002
}
# e211.popitem()
# e211.popitem()
# popitem - убирает последнюю пару в словаре

# pop - удаляет по ключу и возвращает удаленное знаение
mercedes_benz = e211.pop("car_name")
# e211.pop("car_name") KeyError
print(mercedes_benz)
print(e211)

# res1 if cond1 else res2
# print("elem") if 2 != 2 else print("nolo")
e211["color"] = "silver"
e211.update({"volume": 5.5})
e211.update({"model": "w213"})
print(e211)
# update - обновляет значение по ключу если ключа нет то доюавляет новую пару

# get - вытаскивает значение по ключу
# get - принимает 2 аргумента, 1 - ключ, 2 - значение по умолчанию
print(e211['class'])
print(e211.get('class'))

# keys, values, items
print(e211.keys()) # выдает список ключей
print(e211.values()) # выдает список значений
print(e211.items()) # выдает список и ключей и значений [('price', 20000000), ...]

"=================Итерация словарей================="

# for ffff in [1,2,3,4,56,7,8]:
#     print(ffff)

# for days in ["mon", "tue", "wen", "thur"]:
#     print(days)

# print(e211)
e211 = {
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
}

cars = [{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 400000, 
    'model': 'w203', 
    'class': 'C', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w211', 
    'class': 'E', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
},{
    'price': 20000000, 
    'model': 'w204', 
    'class': 'C', 
    'year': 2002, 
    'color': 'silver', 
    'volume': 5.5
}]

filtered_dict = []
for car in cars:
    if car["class"] == "C":
        filtered_dict.append(car)

print(filtered_dict)

# for i in e211:
#     print(i)

# e211.values() == [20000000, 'w213', ...]

# for i in e211.values(): 
#     print(i)

# for val, key in e211.items():
#     print(key, val)

# name, age = ["ertay",20]
# print(name)
# print(age)
print(type({}))
print(type({"":""}))