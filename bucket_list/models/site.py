class Site:
    def __init__(self, name, description, star_rating, city, id=None):
        self.name = name
        self.description = description
        self.star_rating = star_rating
        self.city = city
        self.id = id