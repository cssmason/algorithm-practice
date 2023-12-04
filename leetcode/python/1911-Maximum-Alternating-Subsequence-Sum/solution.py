from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven, sumOdd = 0, 0
        for i in range(len(nums)-1, -1, -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd
        return sumEven


if __name__ == '__main__':
    nums = [4, 2, 5, 3]
    print(Solution().maxAlternatingSum(nums))
