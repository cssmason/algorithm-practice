class Solution:
    # solution 1
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i-1]) + int(chars[i]))
        return ''.join(chars)

    # solution 2
    # def replaceDigits(self, s: str) -> str:
        # return ''.join(chr(ord(s[i-1]) + int(s[i])) if i % 2 != 0 else s[i] for i in range(len(s)))
        
if __name__ == '__main__':
    s = "a1c1e1"
    print(Solution().replaceDigits(s))