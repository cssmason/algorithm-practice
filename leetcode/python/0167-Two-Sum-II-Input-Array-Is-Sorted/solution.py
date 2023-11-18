from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left+1, right+1]
        return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
