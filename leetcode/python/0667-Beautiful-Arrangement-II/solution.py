from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        left, right = 1, n
        for i in range(k):
            if i % 2 == 0:
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1

        if k % 2 == 0:
            while left <= right:
                res.append(right)
                right -= 1
        else:
            while left <= right:
                res.append(left)
                left += 1

        return res
