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
def new_country_visited():
    countries = country_repository.country_select_all()
    return render_template("visited/new.html", countries = countries)

@visited_blueprint.route("/visited", methods=["POST"])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save_country(country)
    return redirect('/visited')

@visited_blueprint.route('/visited/<id>', methods=['GET'])
def cities_visited(id):
    cities = city_repository.cities_in_country(id)
    return render_template("visited/show.html", cities = cities)
