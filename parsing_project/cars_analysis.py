import pandas as pd

car_data = pd.read_csv('cars.csv')
# print(data)

# data = [{
#     "name":"Umka",
#     "salary": 200000,
#     "department": "IT"
# },
# {
#     "name":"Nikita",
#     "salary": 40000,
#     "department": "HR"
# }]

data = {
    "name": ["Umka", "Nikita"],
    "salary": [200000, 40000],
    "department": ["IT", "HR"]
}

print(data)
excel_like = pd.DataFrame(data)
# max_value = excel_like['salary'].max()
# print(excel_like[excel_like['salary'] == max_value])
# table[column_name] syntax
# print(excel_like['last_name'])

# print(excel_like)
# print(excel_like.loc[0, 'salary'])
# print(excel_like.loc['y', 'x'])

# print(excel_like['name'] == 'Umka')

print(car_data['year'])

print(car_data[(car_data['title'] == 'Toyota Camry VII (XV50) Рестайлинг 2.5 AT') & (car_data['year'].isin(['2016']))])

# dataframe[column_name] condition value
# dataframe[dataframe[column_name] condition value]

# print(5==5 and 7==7)