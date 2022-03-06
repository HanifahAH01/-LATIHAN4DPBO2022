from vehicle import Vehicle

class Airplane(Vehicle):
#constructor
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0
        self.wingslength = 0
#set get
    def setAirplane(self, fueltype, maxpasengger, type, age, wingslength, name):
        self.setVehicle(fueltype, maxpasengger)
        self.setBoolean(0)
        self.type = type
        self.age = age
        self.wingslength = wingslength
        self.name = name
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age
    def getWingslength(self):
        return self.wingslength
#PRINT   
    def printAirplane(self):
        print("============================================")
        print("|                 Airplane                 |")
        print("============================================")
        self.printVehicle()
        print("Type : " + str(self.type))
        print("Age : " + str(self.age) + " Years")
        print("Wings Length : " + str(self.wingslength) + "m")
        
