class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, res = 0, 0, 0
        for i in range(len(s)):
            curr += 1
            if i + 1 < len(s) and s[i] != s[i+1]:
                res += min(prev, curr)
                prev, curr = curr, 0
        return res + min(prev, curr)

if __name__ == '__main__':
    s = "10101"
    print(Solution().countBinarySubstrings(s))