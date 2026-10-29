def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error occured in fun1()")
    print("Leaving fun1")
def fun2():
    print("Entering fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("Error occured in fun2")
        raise e
    finally:
        print("Leaving fun2")
print("Prgm started")
fun1()
print("Prgm ended")
