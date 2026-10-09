import pandas as pd
from sqlalchemy import create_engine

uri = "postgresql+psycopg2://postgres:1@localhost:5432/pagila"
conn = create_engine(uri)

# merge
# concat
# plotly

film = pd.read_sql("select film_id, title, language_id from film", conn)
# language = pd.read_sql("select * from language", conn)
language = pd.DataFrame({
    "language_id": [1,2,3,4,5,6],
    "language": ["russian", "spanish", "english", "kazakh", "aasdf", "asdfasdf"]
})
inventory = pd.read_sql("select * from inventory", conn)
csv_data = pd.read_csv('test.csv')


print(film)
print(language)
print(inventory)

new_film = pd.merge(film, language, how='inner', on='language_id')

print(new_film)

# inner
# left
# right
# full
# cross

new_film = pd.merge(film, language, how='left', on='language_id')
print(new_film)

# NaN
# NaT

new_film = pd.merge(film, language, how='right', on='language_id')
print(new_film)

print(csv_data)

# new_film = pd.merge(film, csv_data, how='left', on='language_id_1')
# print(new_film)

new_film = pd.merge(film, csv_data, how='left', left_on='language_id', right_on='language_id_1')
print(new_film)

# full join
new_film = pd.merge(film, csv_data, how='outer', left_on='language_id', right_on='language_id_1')
print(new_film)

# pd.concat()

actor_names = pd.read_sql("select first_name, last_name from actor", conn)
customer_names = pd.read_sql("select first_name, last_name from customer", conn)

print(actor_names)
print(customer_names)

names = pd.concat([actor_names, customer_names])
print(names.loc[0])

a = pd.DataFrame({"a": [1]})
b = pd.DataFrame({"b": [1, 2]})
test = pd.concat([a, b], ignore_index=True, axis=0)
print(test)

test = pd.concat([a, b], axis=1)
print(test)


test['c'] = test['a'] + test['b']
print(test)

sum_columns = ['a', 'b']

test['c'] = test[sum_columns].sum(axis=0)
print(test)