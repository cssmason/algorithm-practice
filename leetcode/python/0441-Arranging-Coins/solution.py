class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        res = 0
        while left <= right:
            middle = (left+right) // 2
            coins = (middle/2) * (middle + 1)
            if coins > n:
                right = middle - 1
            else:
                left = middle + 1
                res = max(middle, res)
        return res


if __name__ == '__main__':
    n = 5
    print(Solution().arrangeCoins(n))
