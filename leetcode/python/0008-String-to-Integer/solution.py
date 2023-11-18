import math
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        match_str = re.findall(r"^[+-]?\d+", s)

        if not match_str:
            return 0

        INT_MAX = int(math.pow(2, 31) - 1)
        INT_MIN = int(-1 * math.pow(2, 31))
        if int(match_str[0]) > INT_MAX:
            res = INT_MAX
        elif int(match_str[0]) < INT_MIN:
            res = INT_MIN
        else:
            res = int(match_str[0])

        return res
