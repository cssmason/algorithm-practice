import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        res = 0
        initial = 0

        for value in count.values():
            if value % 2 == 1:
                res += value - 1
                initial = 1
            else:
                res += value
        return initial + res
