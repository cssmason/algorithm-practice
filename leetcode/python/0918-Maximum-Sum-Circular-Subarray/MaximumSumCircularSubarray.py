class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = maxSoFar = curMin = minSoFar = nums[0]
        for i in range(1,len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            maxSoFar = max(maxSoFar, curMax)
            curMin = min(nums[i], curMin + nums[i])
            minSoFar = min(minSoFar, curMin)
        
        s = sum(nums)
        if minSoFar == s:
            return maxSoFar

        return max(maxSoFar, s - minSoFar)