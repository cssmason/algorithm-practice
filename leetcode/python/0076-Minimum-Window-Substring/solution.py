import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = collections.Counter(t)
        have, need = 0, len(t_count)
        res, res_len = [None, None], float("inf")
        window_count = {}
        left, right = 0, 0

        while right < len(s):
            char = s[right]
            window_count[char] = 1 + window_count.get(char, 0)

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while left <= right and have == need:
                char = s[left]

                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    have -= 1

                left += 1

            right += 1

        left, right = res

        return s[left: right+1] if res_len != float("inf") else ""
