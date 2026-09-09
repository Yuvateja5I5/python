#count the frequences
str=input("Enter the string:")
str1=""
count=0
for i in str:
    if i  not in str1:
        str1=str1+i
        count=0
        for j in str:
            if i==j:
                count+=1
        print(i,count)
                
    
