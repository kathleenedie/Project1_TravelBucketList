import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()


country1 = Country("Uganda", "Africa")
country_repository.save_country(country1)
country2 = Country("France", "Europe")
country_repository.save_country(country2)

country_repository.country_select_all()


city1 = City("Entebbe", 2012, "Wildlife", "http://www.bbc.co.uk", country1)
city_repository.save_city(city1)
city2 = City("Le Puy", 2005, "Food", "http://guardian.com", country2, True)
city_repository.save_city(city2)
city3 = City("Montpellier", 2014, "Culture", "http://www.montpellier-france.com", country2)
city_repository.save_city(city3)

city_repository.city_select_all()

city_repository.cities_in_country(country2)

pdb.set_trace()