try:
    a=int(input("Enter a value :"))
    b=input("Enter a value :")
    res=a/b
    print(res)
except ZeroDivisionError as e:
    print("It is a zero division error")
except ValueError as e:
    print("It is a value error")
except Exception as e:
    print("Other error")
