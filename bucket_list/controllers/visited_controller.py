from flask import Flask, render_template
from flask import Blueprint
from models.country import Country
from models.city import City



visited_blueprint = Blueprint("visited", __name__)

@visited_blueprint.route('/visited')
def visited():
    return render_template("visited/show.html")