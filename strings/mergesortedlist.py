#count vowels and consonents
str=input("Enter a string:")
vowels="aeiouAEIOU"
count1=0
count2=0
for i in str:
   
    if i in vowels:
        count1+=1
    else:
        count2+=1
print( "vowels=",count1)
print("consonents=",count2)
