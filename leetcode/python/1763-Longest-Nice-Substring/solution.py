class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        S = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in S:
                front = self.longestNiceSubstring(s[:i])
                print(i, '----f', front)
                tail = self.longestNiceSubstring(s[i+1:])
                print(i, '----t', tail)
                # print(max(front, tail, key=len))
                # return max(front, tail, key=len)
        print('result', s)
        return s


if __name__ == '__main__':
    s = "YazaAayuUxX"
    print(Solution().longestNiceSubstring(s))
