from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nTotal = (mean * (m + n)) - sum(rolls)

        if nTotal < n or nTotal > n * 6:
            return []

        res = []
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            res.append(dice)
            nTotal -= dice
            n -= 1
        return res


if __name__ == '__main__':
    rolls = [1, 5, 6]
    mean = 3
    n = 4
    print(Solution().missingRolls(rolls, mean, n))
