import collections
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest, counter = 0, collections.Counter(nums)
        for num in nums:
            if num + 1 in counter:
                longest = max(longest, counter[num] + counter[num + 1])
        return longest

if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    print(Solution().findLHS(nums))