import unittest
from models.city import City

class TestCity (unittest.TestCase):

    def setUp(self):
        self.city = City("Entebbe", 2015, "Wildlife", "http://bbc.co.uk", "Uganda")

    def test_city_has_name(self):
        self.assertEqual("Entebbe", self.city.name)

    def test_city_has_date(self):
        self.assertEqual(2015, self.city.year)

    def test_city_has_category(self):
        self.assertEqual("Wildlife", self.city.category)

    def test_city_has_photo_link(self):
        self.assertEqual("http://bbc.co.uk", self.city.photo_link)
    
    def test_city_has_country(self):
        self.assertEqual("Uganda", self.city.country)
    
    def test_city_intance_is_not_visited(self):
        self.assertEqual(False, self.city.visited)

    def test_city_denote_visited(self):
        self.city.denote_visited()
        self.assertEqual(True, self.city.visited)