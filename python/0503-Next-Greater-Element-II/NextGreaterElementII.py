from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, result = [], [-1] * n
        for i in range(2 * n):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result
        
if __name__ == '__main__':
    nums = [1, 2, 1]
    print(Solution().nextGreaterElements(nums))