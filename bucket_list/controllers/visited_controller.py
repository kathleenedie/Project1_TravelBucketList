from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.city import City

visited_blueprint = Blueprint("visited", __name__)

from repositories import country_repository, city_repository



@visited_blueprint.route('/visited', methods=['GET'])
def index():
    countries = country_repository.country_select_all()
    return render_template("visited/index.html", countries = countries)

@visited_blueprint.route("/visited/new", methods=['GET'])
def new_city_visited():
    countries = country_repository.country_select_all()
    return render_template("visited/new.html", countries = countries)

@visited_blueprint.route("/visited", methods=["POST"])
def create_city():
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)

    country_repository.save_country(country)

    city_name = request.form['city_name']
    year = request.form['year']
    category = request.form['category']
    photo_link = request.form['photo_link']
    visited = request.form['visited']
    city = City(city_name, year, category, photo_link, country, visited)

    city_repository.save_city(city)

    return redirect('/visited')

@visited_blueprint.route('/visited/<id>', methods=['GET'])
def cities_visited(id):
    cities = city_repository.cities_in_country(id)
    return render_template("visited/show.html", cities = cities)

# edit route needed, get request
@visited_blueprint.route("/visited/<id>/edit", methods=["GET"])
def edit_city_visited(id):
    city = city_repository.select_city(id)
    countries = country_repository.select_all()
    return render_template('visited/edit.html', city = city, countries = countries)

# update route needed, put request
@visited_blueprint.route("/visited/<id>", methods=["POST"])
def update_city_visited(id):    
    city_name = request.form['city_name']
    year = request.form['year']
    category = request.form['category']
    photo_link = request.form['photo_link']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select_country(country_id)
    city = City(city_name, year, category, photo_link, country, visited, id)
    return redirect('/visited')