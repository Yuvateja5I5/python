#Normal  enacpsulation#
class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name=val
p1=Person()
p1.setter("Teja")
res=p1.getter()
print(res)
