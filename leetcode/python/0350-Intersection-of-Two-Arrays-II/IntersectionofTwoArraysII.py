from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        return sum([[u] * v for u, v in (counter1 & counter2).items()], [])



if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2, 1]
    print(Solution().intersect(nums1, nums2))
