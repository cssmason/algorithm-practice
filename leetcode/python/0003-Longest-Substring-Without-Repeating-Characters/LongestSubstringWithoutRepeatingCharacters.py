class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        res = 0

        for c in s:
            while c in substr:
                substr = substr[1:]
            else:
                substr += c
                res = max(res, len(substr))
        return res