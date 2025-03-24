class House:
    def __init__(self, houseNumber, street, area, noBeds, price):
        self.houseNumber = houseNumber	
        self.street = street
        self.area = area
        self.noBeds = noBeds
        self.price = price

    def setHouseNumber(self, houseNumber):
        self.houseNumber = houseNumber

    def setStreet(self, street):
        self.street = street

    def setArea(self, area):
        self.area = area

    def setNoBeds(self, noBeds):
        self.noBeds = noBeds
    
    def setPrice(self, price): 
        self.price = price
    
    def getHouseNumber(self):
        return self.houseNumber
    
    def getStreet(self):    
        return self.street
    
    def getArea(self):
        return self.area
    
    def getNoBeds(self):
        return self.noBeds
    
    def getPrice(self):
        return self.price
    
    def display(self):
        print("House Number: ", self.houseNumber)
        print("Street: ", self.street)
        print("Area: ", self.area)
        print("Number of Bedrooms: ", self.noBeds)
        print("Price: ", self.price)

    def updateHouseNumber(self, houseNumber):
        if isinstance(houseNumber, int):
            self.houseNumber = houseNumber
        else:
            raise ValueError("houseNumber must be an integer")

    def updateStreet(self, street):
        if isinstance(street, str):
            self.street = street
        else:
            raise ValueError("street must be a string")

    def updateArea(self, area):
        if isinstance(area, str):
            self.area = area
        else:
            raise ValueError("area must be a string")

    def updateNoBeds(self, noBeds):
        if isinstance(noBeds, int):
            self.noBeds = noBeds
        else:
            raise ValueError("noBeds must be an integer")

    def updatePrice(self, price):
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise ValueError("price must be a number (int or float)")
    
    
print("\n")
print("City/Town houses")
print("\n")

house = House(5, "Main Street", "Blanchardstown", 2, 500000)
house.display()

print("\n")

house.updateHouseNumber(10)
house.updateStreet("High Street")
house.updateArea("Downtown")
house.updateNoBeds(3)
house.updatePrice(600000)

house.display()

print("\n")
print("Country houses")
print("\n")


class countryHouse(House):
    def __init__(self, houseNumber, street, area, noBeds, price, garden, garage):
        super().__init__(houseNumber, street, area, noBeds, price)
        self.garden = garden
        self.garage = garage

    def setGarden(self, garden):
        self.garden = garden

    def setGarage(self, garage):
        self.garage = garage

    def getGarden(self):
        return self.garden

    def getGarage(self):
        return self.garage

    def display(self):
        super().display()
        print("Garden: ", self.garden)
        print("Garage: ", self.garage)

    def updateCountryHouseNumber(self, houseNumber):
        if isinstance(houseNumber, int):
            self.houseNumber = houseNumber
        else:
            raise ValueError("houseNumber must be an integer")

    def updateCountryStreet(self, street):
        if isinstance(street, str):
            self.street = street
        else:
            raise ValueError("street must be a string")

    def updateCountryArea(self, area):
        if isinstance(area, str):
            self.area = area
        else:
            raise ValueError("area must be a string")

    def updateCountryNoBeds(self, noBeds):
        if isinstance(noBeds, int):
            self.noBeds = noBeds
        else:
            raise ValueError("noBeds must be an integer")

    def updateCountryPrice(self, price):
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise ValueError("price must be a number (int or float)")
        
    def updateCountryGarden(self, garden):
        if isinstance(garden, bool):
            self.garden = garden
        else:
            raise ValueError("garden must be a boolean")
        
    def updateCountryGarage(self, garage):
        if isinstance(garage, bool):
            self.garage = garage
        else:
            raise ValueError("garage must be a boolean")


house = countryHouse(12, "Oak Road", "Co. Dublin", 4, 350000, False, True)
house.display()

print("\n")

house.updateCountryHouseNumber(27)
house.updateCountryStreet("Spruce Ave")
house.updateCountryArea("Co. Meath")
house.updateCountryNoBeds(5)
house.updateCountryPrice(400000)
house.updateCountryGarden(True)
house.updateCountryGarage(False)

house.display()

print("\n")
print("Inheritance examples")
print("\n")

house_instance = House(15, "Caffrey Rd", "Co. Galway", 3, 250000)
house_instance.display()

print("\n")


country_house_instance = countryHouse(25, "Birch Cresent", "Co. Offaly", 5, 450000, True, True)
country_house_instance.display()


