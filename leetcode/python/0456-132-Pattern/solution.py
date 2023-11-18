from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        right, stack = float('-inf'), []
        for num in reversed(nums):
            if num < right:
                return True
            else:
                while stack and stack[-1] < num:
                    right = stack.pop()
            stack.append(num)
        return False


if __name__ == '__main__':
    nums = [-1, 3, 2, 0]
    print(Solution().find132pattern(nums))
