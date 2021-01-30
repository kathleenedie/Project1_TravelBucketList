from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.visited_repository as visited_repository

def save_country(country):
    sql = "INSERT INTO countries (name, continent) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    id = results [0]['id']
    country.id = id
    return country

def save_city(city):
    sql = "INSERT INTO cities (name, year, category, photo_link, country_id, visited) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [city.name, city.year, city.category, city.photo_link, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city