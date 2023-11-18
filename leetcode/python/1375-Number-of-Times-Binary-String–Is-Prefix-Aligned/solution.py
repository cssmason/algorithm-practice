from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxNum, res = 0, 0
        for index, flip in enumerate(flips, 1):
            maxNum = max(maxNum, flip)
            res += maxNum == index
        return res
