from time import sleep


class Persons():

#constructor
    def __init__(self):
        self.nik = 0
        self.name = ""
        self.gender = ""
    def setPersons(self, nik, name, gender):
        self.nik = nik
        self.name = name
        self.gender = gender

#set get
    def setNik(self, nik):
        self.nik = nik
     def getNik(self):
        return self.gender

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setGender(self, gender):
        self.gender = gender
    def getGender(self):
        return self.gender
#PRINT
    def printPersons(self):
        print("NIK : " + str(self.nik))
        print("Name : " + str(self.name))
        print("Gender : " + str(self.gender))

    def sleep(self):
        print(str(self.name) + " is sleeping now")