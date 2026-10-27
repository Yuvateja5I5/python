class Heart:
    def __init__(self):
        self.status="single"
class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("car is ready to ride....")
class Person:
    def __init__(self,name):
        self.Pname=name
        self.h=Heart()
        self.c=""
    def hascar(self,p):
        self.c=p
p1=Person("Teja")
c1=car("lamborgibi")
p1.hascar(c1)
print(p1.Pname)
print(p1.h.status)
print(p1.c.cname)
p1.c.getcar()
del p1
print(c1.cname)
c1.getcar()
print(p1.h.status)

        
