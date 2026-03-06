class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1
        return nums
obj=Solution()
print(obj.moveZeroes([0,1,2,0,0,3,4]))