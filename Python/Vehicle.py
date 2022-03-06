class Vehicle():
#constructor
    def __init__(self):
        self.type = ""
        self.maxpasengger = 0
        self.boolean = 0
    def setVehicle(self, type, maxpasengger):
        self.type = type
        self.maxpasengger = maxpasengger
#set get
    def settype(self, type):
        self.type = type
    def gettype(self):
        return self.type
    def setMaxpassengger(self, maxpasengger):
        self.maxpasengger = maxpasengger
    def getMaxpassengger(self):
        return self.maxpasengger
    def setBoolean(self, boolean):
        self.boolean = boolean
    def getBoolean(self):
        return self.boolean
    def printVehicle(self):
        print("Type : " + str(self.type))
        print("Max passenggers : " + str(self.maxpasengger))
#PRINT      
    def move(self, nama):
        if self.boolean == 1:
            print("Ship " + nama + " is move")
        elif self.boolean == 0:
            print("Airship " + nama + " is move")