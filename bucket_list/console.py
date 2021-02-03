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
country3 = Country("Malaysia", "Asia")
country_repository.save_country(country3)
country4 = Country("Argentina", "Americas")
country_repository.save_country(country4)

country_repository.country_select_all()


city1 = City("Entebbe", 0, "Wildlife", None, country1)
city_repository.save_city(city1)
city2 = City("Bezier", 2005, "History", "http://bezier.com", country2, True)
city_repository.save_city(city2)
city3 = City("Troyes", 0, "Food & Drink", None, country2)
city_repository.save_city(city3)
city4 = City("Sandakan", 1997, "History", "http://www.sandakanmarches.co.my", country3, True)
city_repository.save_city(city4)
city5 = City("Bukit Fraser", 1997, "Landscapes", "http://www.birdingonbukitfraser.co.my", country3, True)
city_repository.save_city(city5)
city6 = City("Redang", 0,"Beaches", None, country3)
city_repository.save_city(city6)
city7 = City("Buenos Aires", 2002, "Culture", "www.casarosada.com", country4, True)
city_repository.save_city(city7)
city8 = City("San Salvador de Jujoy", 2020, "Landscapes", "http://paintedhill.com", country4, True)
city_repository.save_city(city8)
city9 = City("Mendoza", 0, "Food & Drink", None, country4)
city_repository.save_city(city9)


city_repository.city_select_all()


pdb.set_trace()