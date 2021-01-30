from flask import Flask, render_template
from flask import Blueprint

from models.country import Country
from models.city import City

visited_blueprint = Blueprint("visited", __name__)

from repositories import country_repository, country_repository



@visited_blueprint.route('/visited')
def visited():
    countries = country_repository.country_select_all()
    return render_template("visited/show.html", countries = countries)
