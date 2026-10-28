class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("car is ready to ride....")
class Person:
    def __init__(self,name):
        self.pname=name
        self.c=""
    def hascar(self,p):
        self.c=p
p1=Person("Teja")
c1=car("innova")
p1.hascar(c1)
print(p1.pname)
print(p1.c.cname)
p1.c.getcar()
del p1
print(c1.cname)
c1.getcar()
