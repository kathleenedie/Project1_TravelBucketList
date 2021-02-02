from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.city import City

visited_blueprint = Blueprint("visited", __name__)

from repositories import country_repository, city_repository


# HOME PAGE
@visited_blueprint.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# DISPLAY ALL COUNTRIES WITH LINK TO CITIES
@visited_blueprint.route('/visited', methods=['GET'])
def index():
    countries = country_repository.country_select_all()
    return render_template("visited/index.html", countries = countries)

# DISPLAY NEW COUNTRY FORM
@visited_blueprint.route("/visited/new", methods=['GET'])
def new_country_visited():
    countries = country_repository.country_select_all()
    return render_template("visited/new.html", countries = countries)

# CREATE NEW COUNTRY RECORD AND SAVE TO COUNTRIES DATABASE TABLE
@visited_blueprint.route("/visited", methods=["POST"])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)

    country_repository.save_country(country)

    return redirect('/visited')

# DISPLAY ALL CITIES WITH A GIVEN COUNTRY ID
@visited_blueprint.route('/visited/<id>', methods=['GET'])
def cities_visited(id):
    cities = city_repository.cities_in_country(id)
    country = country_repository.select_country(id)
    return render_template("visited/show.html", cities = cities, country = country)

# DISPLAY NEW CITY FORM
@visited_blueprint.route('/visited/<id>/new', methods=['GET'])
def new_city_visited(id):
    cities = city_repository.cities_in_country(id)
    country = country_repository.select_country(id)
    
    return render_template("visited/city_new.html", country = country, cities = cities)

# CREATE NEW CITY RECORD AND SAVE TO CITY DATABASE TABLE
@visited_blueprint.route("/visited/<id>", methods=["POST"])
def create_city(id):
    name = request.form['name']
    year = request.form['year']
    category = request.form['category']
    photo_link = request.form['photo_link']
    country = country_repository.select_country(id)
    visited = request.form['visited']
    city = City(name, year, category, photo_link, country, visited)

    city_repository.save_city(city)

    return redirect("/visited/"+id)


@visited_blueprint.route('/visited/<id>/<city_id>', methods=['GET'])
def city_visited(id, city_id):
    # cities = city_repository.cities_in_country(id)
    city = city_repository.select_city(city_id)
    return render_template("visited/show_city.html", city = city)



@visited_blueprint.route("/visited/<id>/<city_id>/edit", methods=["GET"])
def edit_city_visited(id, city_id):
    # cities = city_repository.cities_in_country(id)
    country = country_repository.select_country(id)
    city = city_repository.select_city(city_id)

    return render_template('visited/edit.html', city = city, country=country)

@visited_blueprint.route("/visited/<id>/<city_id>", methods=["POST"])
def update_city_visited(id, city_id):    
    name = request.form['name']
    year = request.form['year']
    category = request.form['category']
    photo_link = request.form['photo_link']
    country = country_repository.select_country(id)
    visited = request.form['visited']
    city = City(name, year, category, photo_link, country, visited, id)
    city_repository.update(city)
    return redirect('/visited/'+id)

# @visited_blueprint.route("/visited/<id>/<city_id>/delete", methods=['POST'])
# def delete_city(id, city_id):
#     city
#     city_repository.delete(city_id)

#     return redirect('/visited/'+id)

@visited_blueprint.route("/destination", methods=['GET'])
def cities_visited_page():
    cities = city_repository.city_select_visited()
    return render_template("destination/index.html", cities = cities)