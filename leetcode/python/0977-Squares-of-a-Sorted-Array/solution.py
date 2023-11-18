from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left]*nums[left] > nums[right]*nums[right]:
                res.append(nums[left]*nums[left])
                left += 1
            else:
                res.append(nums[right]*nums[right])
                right -= 1
        return res[::-1]


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
