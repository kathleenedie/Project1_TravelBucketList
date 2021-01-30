import unittest
from models.country import Country

class TestCountry (unittest.TestCase):
    def setUp(self):
        self.country = Country("Uganda", "Africa")

    def test_country_has_name(self):
        self.assertEqual("Uganda", self.country.name)

    