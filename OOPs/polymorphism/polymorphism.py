class Animal:
    def eat(self):
        print("Animals can eat")
    def walk(self):
        print("Animals can walk")
class dog(Animal):
    def sound(self):
        print("Dog is barking")
class tiger(Animal):
    def sound(self):
        print("Tiger is roaring")
d1=dog()
t1=tiger()
def allow(res):
    res.eat()
    res.walk()
    res.sound()
allow(d1)
allow(t1)
