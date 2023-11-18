class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n, ans = len(s), 0
        for i in range(n):
            if s[i] in 'aeiouAEIOU':
                ans += 1 if i < n // 2 else -1
        return ans == 0


if __name__ == '__main__':
    s = "book"
    print(Solution().halvesAreAlike(s))
