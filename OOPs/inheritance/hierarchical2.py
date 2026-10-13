class Animal:
    def eat(self):
        print("Animlas are eating")
class lion(Animal):
    def non_veg(self):
        print("Lion eat flesh ")
class deer(Animal):
    def veg(self):
        print("Deer eat grass")
l1=lion()
d1=deer()
l1.eat()
l1.non_veg()
d1.eat()
d1.veg()
