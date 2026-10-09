import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine


uri = "postgresql+psycopg2://postgres:1@localhost:5432/pagila"
conn = create_engine(uri)


months = ["Январь", "февраль", "март", "апрель"]
sales = [100, 200, 150, 400]

# fig = px.line(
#     x=months,
#     y=sales
# )

# fig.show()

df = pd.DataFrame({
    "months": ["Январь", "Январь", "февраль", "февраль", "март", "апрель"],
    "sales": [500, 100, 200, 200, 150, 400],
    "city": ["bish", "osh", "osh", "bish", "karakol", "karakol"]
})

# fig = px.line(
#     df,
#     x='months',
#     y='sales',
#     title='test line chart',
#     color='city'
# )

# fig.show()

films = pd.read_sql("""
select extract(year from rental_date) as rental_year, sum(f.rental_rate) as rental_rate from rental as r
    join inventory i
        on r.inventory_id = i.inventory_id
    join film f
        on f.film_id = i.film_id
group by extract(year from rental_date)
""", conn)

print(films)

fig = px.line(
    films,
    x='rental_year',
    y='rental_rate',
    title='rental dashboard',
    # color='city'
)

fig.show()

