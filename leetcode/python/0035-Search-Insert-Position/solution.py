from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))
