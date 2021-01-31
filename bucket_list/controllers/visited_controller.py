from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.city import City

visited_blueprint = Blueprint("visited", __name__)

from repositories import country_repository, city_repository



@visited_blueprint.route('/visited', methods=['GET'])
def index():
    cities = city_repository.city_select_all()
    return render_template("visited/index.html", cities = cities)

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
def city_visited(id):
    city = city_repository.select_city(id)
    return render_template("visited/show.html", city = city)

@visited_blueprint.route("/visited/<id>/edit", methods=["GET"])
def edit_city_visited(id):
    city = city_repository.select_city(id)
    countries = country_repository.country_select_all()
    return render_template('visited/edit.html', city = city, countries = countries)

@visited_blueprint.route("/visited/<id>", methods=["POST"])
def update_city_visited(id):    
    name = request.form['name']
    year = request.form['year']
    category = request.form['category']
    photo_link = request.form['photo_link']
    country = country_repository.select_country(request.form['country_id'])
    visited = request.form['visited']
    city = City(name, year, category, photo_link, country, visited, id)
    # print(city.country.name())
    city_repository.update(city)
    return redirect('/visited')