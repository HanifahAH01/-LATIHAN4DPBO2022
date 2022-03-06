from vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Persons import Persons
from Job import Job
from Driver import Driver

d1 = Driver()
d2 = Driver()
d3 = Driver()
d4 = Driver()
d5 = Driver()
#Driver#
d1.setDriver(11001, "10-08-20003", "Airplane")
d2.setDriver(11002, "06/06/2026", "Airplane")
d3.setDriver(11003, "10/10/2025", "Airplane")
d4.setDriver(11004, "3/4/2025", "Airplane")
d5.setDriver(11005, "16/6/2025", "Airplane")

#Person#
d1.setPersons(10011, "Han", "Famale")
d2.setPersons(20011, "Hani", "Famale")
d3.setPersons(30011, "Hanif", "Male")
d4.setPersons(40011, "Hanifah", "Female")
d5.setPersons(50011, "Humaira", "Famale")

#Job#
d1.setJob(50006, "PT Gundam Sejahtera", "Pilot")
d2.setJob(50007, "PT Mary Go Sejahtera", "Pilot")
d3.setJob(50008, "PT Leveling", "Captain")
d4.setJob(50009, "PT Templ", "Pilot")
d5.setJob(60001, "PT Kultivasi", "Captain")

#PRINT#
d1.printDriver()
d2.printDriver()
d3.printDriver()
d4.printDriver()
d5.printDriver()
print("#########################################################################################")

A = Airplane()
A2 = Airplane()
A3 = Airplane()
A4 = Airplane()
A5 = Airplane()

A.setAirplane("Han", 900, "A", 18, 40, "Boeing")
A2.setAirplane("Hani", 700, "B", 20, 90, "Boeing")
A3.setAirplane("Hanif", 1000, "D", 9, 100, "Boeing")
A5.setAirplane("Humaira", 933, "C", 17, 20, "Boeing")
A4.setAirplane("Hanifah", 333, "D", 19, 30, "Boeing")

#PRINT#
A.printAirplane()
A2.printAirplane()
A3.printAirplane()
A4.printAirplane()
A5.printAirplane()
print("#########################################################################################")

Type=["A", "B", "C", "D", "D", "E"]
name=["han", "Hani", "hanif", "Hanifah", "Humaira"]
maxpasengger=["500", "2678", "900", "7658", "1256"]
age=["9", "14", "25", "28", "10"]
type=["B1", "C", "H", "C2", "D"]
Country=["Korea", "Indonesa", "inggris", "jepang", "Australia"]

S = [Ship() for i in range(5)]

for i in range(5):
        S[i].setname(name[i])
        S[i].setType(Type[i])
        S[i].setmaxpassanger(maxpasengger[i])
        S[i].setAge(age[i])
        S[i].setCountry(Country[i])

for i in range(5):
    S[i].printShip()
print("#########################################################################################")