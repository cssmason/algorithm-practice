import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        for i, j, m, n in itertools.permutations(arr):
            if i * 10 + j < 24 and m * 10 + n < 60:
                return '{}{}:{}{}'.format(i, j, m, n)
        return ""
