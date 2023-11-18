class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


if __name__ == '__main__':
    s = "baabb"
    print(Solution().removePalindromeSub(s))
