class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in seen:
                return seen[k],i
            else:
                seen[nums[i]]=i
obj=Solution()
print(obj.twoSum([7,2,5,8],9))