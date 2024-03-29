from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
