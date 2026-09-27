n=input("Enter a string:")
ch=input("enter character to check:")
def count_char(n):
    count=0
    for i in n:
        
        if i==ch:
            count=count+1
    print(count)
count_char(n)
        
  
