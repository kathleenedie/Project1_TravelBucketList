class City:
    def __init__(self, name, year, category, photo_link, country, visited = False, id = None):
        self.name = name
        self.year = year
        self.category = category
        self.photo_link = photo_link
        self.country = country
        self.visited = visited
        self.id = id

    def denote_visited(self):
        self.visited = True