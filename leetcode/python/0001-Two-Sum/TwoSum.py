from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for index, value in enumerate(nums):
            if target - value in numMap:
                return [numMap[target - value], index]
            numMap[value] = index


if __name__ == '__main__':
    nums = [2, 3, 5, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))