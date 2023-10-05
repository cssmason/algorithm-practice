from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = None, 0
        for num in nums:
            if count == 0:
                major = num
            count += (1 if num == major else -1)
        return major


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
