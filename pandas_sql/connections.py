import pandas as pd
from sqlalchemy import create_engine

# pandas - работа с таблицами
# sqlalchemy - работа с базами данных
# psycopg2 - драйвер для postgresql

uri = "postgresql+psycopg2://user:password@host:port/database"

uri = "postgresql+psycopg2://postgres:1@localhost:5432/pagila"
conn = create_engine(uri)

dataframe = pd.read_sql("select * from actor", conn)

dataframe_a = pd.read_sql("select * from customer where first_name like 'A%%'", conn)

# pd.read_excel()
# pd.read_json()

print(dataframe)
print(dataframe_a['first_name'])

# "select count(first_name) from customer where first_name like 'A%%'"

print("hello world")

# dataframe
# series

print(dataframe.head(3)) # limit

# select first_name, last_name from actor
# print(dataframe[['first_name', 'last_name']])

print(dataframe[dataframe['first_name'].str.startswith('A')]) # where 
# dataframe[dataframe['column'] condition]

# print(dataframe[dataframe['actor_id'] == 1])

print(dataframe[
    (dataframe['first_name'].str.startswith('A')) & 
    (dataframe['last_name'].str.startswith('B'))]
)

# == - =
# & - and 
# | - or
# ~ - not
# startswith - like 'A%'
# endswith - like '%A'


# where (condition1) and (condition2)

a = {
    "a" : [1,2,3,4,5],
    "b": ["hello", "hello", "hello", "hello", "bye"]
}

dataframe_a = pd.DataFrame(a)
# print(dataframe_a)

#column
# row    value

# loc
# iloc

dataframe_a.index = ["a", "b", "c", "d", "e"]

# print(dataframe_a)
print(dataframe_a.loc["a"])
print(dataframe_a.iloc[0])

# loc - названию индекса
# iloc - по позиции


# print(dataframe_a.loc["a", "b"])
# print(dataframe_a.iloc[0, 1])

print(dataframe_a.iloc[1:4])
print(dataframe_a.loc["b":"d"])

condition = dataframe["last_name"].str.endswith("S")

print(condition)

# print(dataframe.loc[condition])

dataframe.loc[condition, "last_name"] = "Nikitov"

print(dataframe[condition])
print(dataframe.loc[condition])

# update set = 'nikitov' where last_name like '%S'

dataframe.loc[:, "age"] = 25
print(dataframe)
# alter table add column age
# update table set age = 25

# group by

df = pd.DataFrame(
    {
        "city": ["bishkek", "bishkek", "osh", "karakol", "balykchy"],
        "salary": [100000, 120000, 90000, 70000, 110000],
        "name": ["umka", "nikita", "aidyn", "kamila", "daria"],
        "rating": [5, 2, 1, 5, 5]
    }
)
print(df)

print(df.groupby("city")["salary"].sum())

# select column, aggregate_function(column2)
# group by column

# df.groupby(column)["column2"].aggregate_function()

# sum - sum
# avg - mean
# max - max
# min - min
# count - count


print(df.groupby("city")["salary"].agg(["sum", "mean"]))

print(df.groupby("city").agg({"salary": "sum", "rating":"mean"}))

print(df.groupby("city")["salary"].mean())

df['avg_salary'] = df.groupby("city")["salary"].transform("mean")
print(df)

df = pd.DataFrame({
    "department": [
        "IT", "IT", "HR", "HR", "Finance",
        "Finance", "Marketing", "Marketing", "IT", "Finance"
    ],
    "employee": [
        "alex", "brian", "diana", "emily", "frank",
        "george", "helen", "irene", "jack", "kevin"
    ],
    "salary": [
        150000, 180000, 95000, 110000, 200000,
        175000, 120000, 135000, 160000, 190000
    ],
    "rating": [
        5, 4, 3, 5, 5,
        4, 3, 5, 4, 5
    ],
    "city": [
        "Bishkek", "Osh", "Bishkek", "Osh", "Bishkek",
        "Karakol", "Osh", "Bishkek", "Karakol", "Bishkek"    
]})

print(df)

# 1 Айзат А
# 2 Мария
# 3 Айжаркын
# 4 Айзат М
# 5 Дарья
# 6 Бексултан

# 7
condition = df['city'] == 'Bishkek'
df.loc[condition, 'rating'] = 5
print(df)

print(df.iloc[0:3])
print(df.iloc[3:7])
print(df.iloc[:, 0:3])
print(df.iloc[0:5, 0:2])

condition1 = df["employee"].str.startswith(("a", "b"))
print(df.loc[condition1])

condition2 = df["employee"].str.endswith(("n"))
print(df[condition2])

result = df[(df['department'] == 'IT') & (df['rating'] >= 4)]