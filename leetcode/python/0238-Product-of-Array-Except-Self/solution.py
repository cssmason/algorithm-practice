from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] *= prefix
            res[n - i - 1] *= postfix
            prefix *= nums[i]
            postfix *= nums[n - i - 1]

        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
