class Solution:
    def isPalindrome(self, x):
        x=str(x)
        return x==x[::-1]
s1=Solution()
x=12241
print(s1.isPalindrome(x))
        
        
