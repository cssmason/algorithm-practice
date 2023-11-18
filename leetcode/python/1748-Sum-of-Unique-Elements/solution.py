from typing import List
import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sum(key for key, value in counter.items() if value == 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print(Solution().sumOfUnique(nums))
