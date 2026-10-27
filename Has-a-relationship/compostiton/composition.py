class Heart:
    def __init__(self):
        self.status="single"
class Person:
    def __init__(self,name):
        self.Pname=name
        self.h=Heart()
        print("Welcome to persons Heart")
p1=Person("Teja")
print(p1.Pname)
print(p1.h.status)
del p1
print(p1.h.status)
        
