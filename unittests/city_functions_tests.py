import unittest

from city_functions import city_country_information

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name = city_country_information("santiago", "chile")
        self.assertEqual(city_country_name,"Santiago Chile")

if __name__ == '__main__':
    unittest.main()

