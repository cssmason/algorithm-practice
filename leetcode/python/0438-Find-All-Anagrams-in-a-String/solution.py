import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_count = collections.Counter(p)
        distincts = len(p_count)
        left, right = 0, 0

        while right < len(s):
            if s[right] in p_count:
                p_count[s[right]] -= 1
                if p_count[s[right]] == 0:
                    distincts -= 1

            if right - left + 1 < len(p):
                right += 1
            else:
                if distincts == 0:
                    res.append(left)

                if s[left] in p_count:
                    p_count[s[left]] += 1
                    if p_count[s[left]] == 1:
                        distincts += 1

                left += 1
                right += 1

        return res
