n=input("Enter a string:")
def palindrome(n):
    rev=""
    for i in n:
        rev=i+rev
    if rev==n:
        print("Palindrome")
    else:
        print("not a palindrome")
palindrome(n)
