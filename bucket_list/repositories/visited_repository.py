from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository


def save_city(city):
    sql = "INSERT INTO cities (name, year, category, photo_link, country_id, visited) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [city.name, city.year, city.category, city.photo_link, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)
