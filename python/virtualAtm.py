print("WELCOME TO ATM")
card=int(input("Enter your card:"))
if card==1:
    lang = int(input(" select your language :"))
    if lang==1 or lang==2 or lang==3:
        print("Enter the pin")
    else:
        print("please select the language properly")
    pin = int(input("enter pin:"))
    if pin == 1234:
        option = int((input("enter your option:\n 1. Balance enquiry\n 2.withdrawl\n 3:deposit\n")))
        bal=10000
        if option==1:
           print("your balance is:",bal)
        elif option==2:
            wd=int(input("enter the amount:"))
            if wd<=bal:
                print("transaction is being processed")
                print("Do u want to display the balance")
                user = input("enter your choice:")
                if user == "yes":
                    print("your balance is:", bal - wd)
                    print("Thank you visit again")
                else:
                    print("thank you")
            else:
                print("insufficient balance")
        elif option==3:
            dep=int(input("Enter the deposit amount:"))
            print("your deposit amount is:",dep)
            print("Do u want to display the balance")
            user = input("enter your choice:")
            if user == "yes":
                print("your balance is:", bal + dep)
                print("Thank you visit again")
            else:
                print("thank you")

        else:
            print("please enter option correctly")


    else:
        print("enter pin correctly")
else:
    print("insert card properly")










