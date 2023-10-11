class Solution:

    def longestPalindrome(self, s: str) -> str:
        # Solution 1: Brute force
        # resLen, left, right = 0, 0, 0
        # if not s:
        #     return ""

        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         substr = s[i:j+1]
        #         if self.isPalindrome(substr) and len(substr) > resLen:
        #             resLen = len(substr)
        #             left, right = i, j
        # res = s[left:right+1]

        # return res

        # def isPalindrome(self, s):
        #     if not s:
        #         return False
        #     return s == s[::-1]

        # Solution 2: Dynamic Programming
        res = ""
        resLen = 0

        for i in range(len(s)):
            left, right = i, i

            while left > 0 and s[left-1] == s[left]:
                left -= 1

            while right < len(s) - 1 and s[right+1] == s[right]:
                right += 1

            while left > 0 and right < len(s) - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            if (right - left + 1) > resLen:
                res = s[left:right+1]
                resLen = right - left + 1

                if resLen == len(s):
                    break

        return res


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
