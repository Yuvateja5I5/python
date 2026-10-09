def main():
    str=input("enter a string:")
    return str
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Entering into inner")
        res=ptr()
        result=res.upper()
        print(result)
        print("Leaving from inner")
    return inner
ref=outer(main)
ref()
