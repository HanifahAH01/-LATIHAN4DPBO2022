from Persons import Persons
from Job import Job
from vehicle import Vehicle

class Driver(Persons, Job):
#constructor
    def __init__(self):
        self.lisence = ""
        self.activeuntil = ""
        self.vehicletype = ""
    def setDriver(self, lisence, activeuntil, vehicletype):
        self.lisence = lisence
        self.activeuntil = activeuntil
        self.vehicletype = vehicletype
#set get
    def setLisence(self, lisence):
        self.lisence = lisence
    def getLisence(self):
        return self.lisence

    def setActiveUntil(self, activeuntil):
        self.activeuntil = activeuntil
    def getActiveUntil(self):
        return self.activeuntil

    def setVehicleType(self, vehicletype):
        self.vehicletype =vehicletype
    def getVehicleType(self):
        return self.vehicletype

#PRINT
    def printDriver(self):
        print("============================================")
        print("|                  Drive                   |")
        print("============================================")
        self.printPersons()
        self.sleep()
        print("Lisence ID : " + str(self.lisence))
        print("Active Until : " +  str(self.activeuntil))
        print("Vehicle Type : " + str(self.vehicletype))
        self.printJob()
        