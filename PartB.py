import unittest
from PartA import House, countryHouse  

class TestClassInstances(unittest.TestCase):
    def test_house_instance(self):
        house = House(15, "Elm Street", "Co. Galway", 3, 250000)
        self.assertIsInstance(house, House)

    def test_country_house_instance(self):
        country_house = countryHouse(25, "Maple Avenue", "Co. Cork", 5, 450000, True, True)
        self.assertIsInstance(country_house, countryHouse)

    def test_country_house_is_not_house(self):
        country_house = countryHouse(25, "Maple Avenue", "Co. Cork", 5, 450000, True, True)
        self.assertIsInstance(country_house, House)  
        self.assertNotEqual(type(country_house), House) 

if __name__ == "__main__":
    unittest.main()