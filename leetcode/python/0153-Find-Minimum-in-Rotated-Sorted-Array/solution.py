from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            m = (left+right) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        return res


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))
