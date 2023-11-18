from typing import List


class Solution:
    # Solution 1:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(nums: List[int], max: int):
            ans, curr = 0, 0
            for num in nums:
                if num <= max:
                    curr += 1
                    ans += curr
                else:
                    curr = 0
            return ans

        return count(nums, right) - count(nums, left - 1)

    # Solution 2:
    # def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
    #     ans = 0
    #     l, r = -1, -1
    #     for i, num in enumerate(nums):
    #         if num >= left:
    #             r = i
    #         if num > right:
    #             l = i
    #         ans += (r - l)
    #     return ans
