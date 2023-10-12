from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))