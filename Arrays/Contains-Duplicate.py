class Solution:
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False
obj=Solution()    
print(obj.containsDuplicate([1,2,3]))