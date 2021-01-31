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

def city_select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['year'], row['category'], row['photo_link'], row['country_id'], row['visited'])
        cities.append(city)
    return cities

def select_city(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select_country(result['country_id'])
        city = City(result['name'], result['year'], result['category'], result['photo_link'], country, result['id'] )
    return city

def cities_in_country(id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['year'], row['category'], row['photo_link'], row['country_id'], row['visited'])
        cities.append(city)
    return cities



def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)
