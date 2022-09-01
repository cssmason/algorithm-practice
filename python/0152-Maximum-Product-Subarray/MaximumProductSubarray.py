class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax  = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMin * n
            curMin = min(curMin * n, curMax * n, n)
            curMax = max(tmp, curMax * n, n)
            res = max(res, curMax)
        return res
            