n=input("enter a string:")
def count_vowel(n):
    vowels="aeiouAEIOU"
    count=0
    for  i in n:
        if i in vowels:
            count+=1
    print(count)
count_vowel(n)
    
    
