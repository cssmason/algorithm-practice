from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1:
        # return len(nums) != len(set(nums))

        # solution 2:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(nums))
