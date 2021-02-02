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
        country = country_repository.select_country(row['country_id'])
        city = City(row['name'], row['year'], row['category'], row['photo_link'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

def select_city(city_id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [city_id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select_country(result['country_id'])
        city = City(result['name'], result['year'], result['category'], result['photo_link'], country, result['visited'], result['id'] )
    return city

def update(city):
    sql = "UPDATE cities SET (name, year, category, photo_link, country_id, visited) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.year, city.category, city.photo_link, city.country.id, city.visited, city.id]
    run_sql(sql, values)


def cities_in_country(id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s AND visited = False"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['year'], row['category'], row['photo_link'], row['country_id'], row['visited'], row['id'])
        cities.append(city)
    return cities


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def city_select_visited():
    cities = []
    sql = "SELECT * FROM cities WHERE visited = True"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select_country(row['country_id'])
        city = City(row['name'], row['year'], row['category'], row['photo_link'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

    # sorted_cities = []
    # for city in cities:
    #     key = city.country.id
    #     if key not in sorted_cities:
    #         sorted_cities[city.country.id]
    #     sorted_cities[key].append(city)
    # return sorted_cities

def categories_of_cities(category):
    cities = []
    sql = "SELECT * FROM cities WHERE category = %s AND visited = True"
    values = [category]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['year'], row['category'], row['photo_link'], row['country_id'], row['visited'], row['id'])
        cities.append(city)
    return cities