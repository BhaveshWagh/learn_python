import unittest

from city_functions2 import city_country_information2

class CitiesTestCase(unittest.TestCase):
    def test_city_country2(self):
        city_country_name2 = city_country_information2("santiago","chile")
        self.assertEqual(city_country_name2,"Santiago, Chile")

    def city_country_population(self):
        city_country_pop = city_country_information2("santiago","chile",5000000)
        self.assertEqual(city_country_pop,"Santiago , Chile = population 5000000")

if __name__ == '__main__':
    unittest.main()
