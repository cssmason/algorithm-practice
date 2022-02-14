from cmath import inf
from json.encoder import INFINITY
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingHere, maxSofFar = -inf, -inf
        for num in nums:
            maxEndingHere = max(maxEndingHere + num, num)
            maxSofFar = max(maxSofFar, maxEndingHere)
        return maxSofFar

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
        