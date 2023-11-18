from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMin * n
            curMin = min(curMin * n, curMax * n, n)
            curMax = max(tmp, curMax * n, n)
            res = max(res, curMax)
        return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))
