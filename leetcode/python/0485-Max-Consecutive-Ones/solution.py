from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, result = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                if count > result:
                    result = count
            else:
                count = 0
        return result


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
