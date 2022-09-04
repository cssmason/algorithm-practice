class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        i, j = 0, 0
        while j < len(s):
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            if i == j:
                j += 1
            else:
                i += 1
        return res