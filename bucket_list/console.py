import pdb
from models.country import Country
from models.city import City

import repositories.visited_repository as visited_repository

country1 = Country("Uganda", "Africa")
visited_repository.save_country(country1)
country2 = Country("France", "Europe")
visited_repository.save_country(country2)


city1 = City("Entebbe", 2012, "Wildlife", "http://www.bbc.co.uk", country1)
visited_repository.save_city(city1)
city2 = City("Le Puy", 2005, "Food", "http://guardian.com", country2, True)
visited_repository.save_city(city2)



pdb.set_trace()