from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res


if __name__ == '__main__':
    text = "nlaebolko"
    print(Solution().maxNumberOfBalloons(text))
