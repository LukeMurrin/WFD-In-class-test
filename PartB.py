import unittest
from PartA import House, countryHouse  

class TestClassInstances(unittest.TestCase):
#B2
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

#B3

    def test_house_is_not_country_house(self):
        house = House(15, "Elm Street", "Co. Galway", 3, 250000)
        self.assertNotIsInstance(house, countryHouse)

    def test_country_house_is_not_other_class(self):
        country_house = countryHouse(25, "Maple Avenue", "Co. Cork", 5, 450000, True, True)
        self.assertNotIsInstance(country_house, str)

#B4
 
    def test_objects_are_identical(self):
        house1 = House(15, "Elm Street", "Co. Galway", 3, 250000)
        house2 = house1 
        self.assertIs(house1, house2)  

    def test_objects_are_not_identical(self):
        house1 = House(15, "Elm Street", "Co. Galway", 3, 250000)
        house2 = House(15, "Elm Street", "Co. Galway", 3, 250000)
        self.assertIsNot(house1, house2)

#B5

    def test_update_house_attributes(self):
        house = House(15, "Elm Street", "Co. Galway", 3, 250000)
        
        house.updateHouseNumber(20)
        house.updateStreet("Oak Street")
        house.updateArea("Co. Dublin")
        house.updateNoBeds(4)
        house.updatePrice(300000)
        
        self.assertEqual(house.getHouseNumber(), 20)
        self.assertEqual(house.getStreet(), "Oak Street")
        self.assertEqual(house.getArea(), "Co. Dublin")
        self.assertEqual(house.getNoBeds(), 4)
        self.assertEqual(house.getPrice(), 300000)

    def test_update_country_house_attributes(self):
        country_house = countryHouse(25, "Maple Avenue", "Co. Cork", 5, 450000, True, True)
        
        country_house.updateCountryHouseNumber(30)
        country_house.updateCountryStreet("Pine Lane")
        country_house.updateCountryArea("Co. Limerick")
        country_house.updateCountryNoBeds(6)
        country_house.updateCountryPrice(500000)
        country_house.updateCountryGarden(False)
        country_house.updateCountryGarage(False)
        
        self.assertEqual(country_house.getHouseNumber(), 30)
        self.assertEqual(country_house.getStreet(), "Pine Lane")
        self.assertEqual(country_house.getArea(), "Co. Limerick")
        self.assertEqual(country_house.getNoBeds(), 6)
        self.assertEqual(country_house.getPrice(), 500000)
        self.assertFalse(country_house.getGarden())
        self.assertFalse(country_house.getGarage())

#B6

if __name__ == "__main__":
    unittest.main()