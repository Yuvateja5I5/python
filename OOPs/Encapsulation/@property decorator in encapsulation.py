# @property decorator in encapsulation
class laptop:
    def __init__(self):
        self.__name=""
    @property
    def display(self):
        return self.__name
    @display.setter
    def display(self,val):
        self.__name=val
l1=laptop()
l1.display="Dell"
res=l1.display
print(res)
