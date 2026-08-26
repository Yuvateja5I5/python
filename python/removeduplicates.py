class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        v=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[v]=nums[i]
                v+=1
        return v
s1=Solution()
nums=[1,1,3,3,5,5,7,7]
k=s1.removeDuplicates(nums)
print(nums[:k])

            
        
