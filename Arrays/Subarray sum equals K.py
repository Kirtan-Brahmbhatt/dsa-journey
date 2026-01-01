class Solution:
    def subarraySum(self, nums, k):
        count = 0
        n = len(nums)

        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum += nums[j]

                if currentSum == k:
                    count += 1

        return count


# ----- User Input -----
nums = list(map(int, input("Enter array values: ").split()))
k = int(input("Enter k: "))

obj = Solution()
print(obj.subarraySum(nums, k))
