class Person:
    def __init__(self):
        self.__names=""
    def getter(self):
        return self.__names
    def setter(self,str):
         self.__names=str
    getset=property(getter,setter)
p1=Person()
p1.getset="Yuvateja"
res=p1.getset
print(res)
