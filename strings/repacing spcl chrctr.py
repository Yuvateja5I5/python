str=input("Enter a string:")
str1=""
for i in str:
    if i=='a':
        str1=str1+'@'
    else:
        str1=str1+i
print(str1)
