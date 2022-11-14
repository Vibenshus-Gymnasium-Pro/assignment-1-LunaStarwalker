#Python Crash Course, exercise 11-1, test

import unittest
from city_functions import city_function


class CityFunctionsTest(unittest.TestCase):

    def test_city_country(self):
        formatted_pair = city_function("copenhagen", "denmark")
        self.assertEqual(formatted_pair, "Copenhagen, Denmark")

    def test_city_country_population(self):
        formatted_value = city_function("copenhagen", "denmark", 1000000)
        self.assertEqual(formatted_value, "Copenhagen, Denmark - population 1000000")


unittest.main()
