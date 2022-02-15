from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        unique = set(nums)
        for i in range(1, len(nums)+1):
            if i not in unique:
                result.append(i)
        return result

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))