#first non reapeating character
str=input("Enter a string:")
str1=""
for i in str:
    
    if str.count(i)==1:
        print("Non- repeating character is:",i)
        break
    else:
        str1=str1+i
print(str1)
    
