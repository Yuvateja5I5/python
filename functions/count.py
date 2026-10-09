n=int(input("Enter a digit:"))
def count_digit(n):
    if n==0:
        return 1
    count=0
    while n>0:
        count=count+1
        n=n//10
    print(count)
    
count_digit(n)
    
