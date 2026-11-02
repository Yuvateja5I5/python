l=[]
i=0
while True:
    num=int(input("Enter a num:"))
    l.insert(i,num)
    i=i+1
    print("Do you want to continue")
    print("Press 1.Yes 2.No")
    choice=int(input())
    if choice==1:
        continue
    else:
        break
print(l)
            
            
