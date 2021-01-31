from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save_country(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results [0]['id']
    country.id = id
    return country

def country_select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['continent'], row['id'] )
        countries.append(country)
    return countries



def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)