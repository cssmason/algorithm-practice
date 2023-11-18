class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for char in 'abc':
                    if (i == 0 or s[i-1] != char) and (i == len(s) - 1 or s[i+1] != char):
                        s[i] = char
                        break
        return ''.join(s)


if __name__ == '__main__':
    s = "?zs"
    print(Solution().modifyString(s))
