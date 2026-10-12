class Animal:
    def eat(self):
        print("A eat food")
    def sleep(self):
        print("A is sleeping")
    def sound(self):
        print("A makes sound")
class dog(Animal):
    pass
class cat(Animal):
    pass
class tiger(Animal):
    pass
d1=dog()
c1=cat()
t1=tiger()
d1.eat()
d1.sleep()
d1.sound()
