#first reapeating character
str=input("Enter a string:")
str1=""
for i in str:
    str1+str+i
    if i not in str1:
        print("first repeating character is:",i)
        break
    else:
        str1=str1+i
    
