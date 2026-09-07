#reverse a sentence
str=input("Enter a sentence:")
str1=""
for i in str.split():
    str1=i+" "+str1
print(str1)
