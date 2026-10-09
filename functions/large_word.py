n=input("Enter a sentence:")
def large_word(n):
    res=n.split()
    large=""
    for i in res:
        if len(i)>len(large):
            large=i
    print(large)
    
large_word(n)
