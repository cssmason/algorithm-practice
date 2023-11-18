from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start, ln = 0, len(nums)
        for i in range(ln):
            if i + 1 < ln and nums[i+1] == nums[i] + 1:
                continue
            if i == start:
                result.append(str(nums[start]))
            else:
                result.append(f'{nums[start]}->{nums[i]}')
            start = i + 1
        return result


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
