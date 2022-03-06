class Job():
#constructor
    def __init__(self):
        self.nip = 0
        self.companyname = ""
        self.position = ""
    def setJob(self, nip, companyname, position):
        self.nip = nip
        self.companyname = companyname
        self.position = position
#set get
    def setNip(self, nip):
        self.nip = nip
    def getNip(self):
        return self.nip

    def setCompanyname(self, companyname):
        self.companyname = companyname
    def getCompanyname(self):
        return self.companyname

    def setPosition(self, position):
        self.position =position
    def getPosition(self):
        return self.position
#PRINT
    def printJob(self):
        print("NIP : " + str(self.nip))
        print("Company Name : " + str(self.companyname))
        print("Position : " + str(self.position))
        