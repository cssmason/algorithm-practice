from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        elif sum(num < 0 for num in nums) % 2 == 0:
            return 1
        else:
            return -1
            
if __name__ == '__main__':
    nums = [-1, -2, -3, -4, 3, 2, 1]
    print(Solution().arraySign(nums))