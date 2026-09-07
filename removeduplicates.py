#remove duplicates in string
str=input("Enter a string:")
str1=""
for i in str:
    if i in str1:
        pass
    else:
        str1=str1+i
print(str1)
