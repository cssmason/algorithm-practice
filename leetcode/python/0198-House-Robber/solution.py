from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
