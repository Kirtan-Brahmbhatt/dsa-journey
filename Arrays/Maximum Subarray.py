class Solution:
    def maxSubArray(self, nums):
        m_sum=nums[0]
        c_sum=0
        for i in nums:
            if c_sum < 0:
                c_sum=0
            c_sum+=i
            if c_sum > m_sum:
                m_sum=c_sum
        return m_sum
obj=Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))