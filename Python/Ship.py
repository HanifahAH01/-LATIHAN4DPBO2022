from vehicle import Vehicle
class Ship(Vehicle):
#constructor
    def __init__(self):
        self.age = 0
        self.type = ""
        self.country = ""
        self.name = ""
        self.maxpasengger=0
#set get   
    def setname(self, name):
        self.name=name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type
    def setCountry(self, country):
        self.country = country
    def getCountry(self):
        return self.country
    def setmaxpassanger(self, maxpasengger):
        self.maxpasengger=maxpasengger
    def getMaxpassengger(self, maxpasengger):
        self.maxpasengger+maxpasengger
#PRINT
    def printShip(self):
        print("============================================")
        print("|                  Ship                    |")
        print("============================================")
        self.printVehicle()
        #Sself.move(self.name)
        print("Name :" + str(self.name))
        print("Type :" + str(self.type))
        print("Age : " + str(self.age ))
        print("Country Manufacture : " + str(self.country))
        