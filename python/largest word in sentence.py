#largest word in sentence
str=input("Enter a sentence:")
str1=str.split()
largest=str1[0]
for word in str1:
    if len(word)>len(largest):
        largest=word
print(largest)
    
    
    
