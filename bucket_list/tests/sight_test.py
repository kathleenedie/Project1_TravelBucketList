import unittest
from models.sight import Sight

class TestSight (unittest.TestCase):

    def setUp(self):
        self.sight = Sight("Botanic Gardens", "public gardens", 5, "Entebbe")

    def test_sight_has_name(self):
        self.assertEqual("Botanic Gardens", self.sight.name)

    def test_sight_has_description(self):
        self.assertEqual("public gardens", self.sight.description)
    
    def test_sight_as_star_rating(self):
        self.assertEqual(5, self.sight.star_rating)
    
    def test_sight_has_city(self):
        self.assertEqual("Entebbe", self.sight.city)