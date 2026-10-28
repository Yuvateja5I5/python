def fun1():
    print("Inside fun1")
    try:
        fun2()
    except Exception as e:
        print("error occured in fun1")
    print("Leaving fun1")
def fun2():
    print("Entering fun2")
    res=10/0
    print(res)
    print("Leaving fun2")
print("Program started")
fun1()
print("program ended")
