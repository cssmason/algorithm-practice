class Solution:
    def secondHighest(self, s: str) -> int:
        res = sorted(set([int(char) for char in s if char.isdigit()]), reverse=True)
        return res[1] if len(res) > 1 else -1

if __name__ == '__main__':
    s = "dfa12321afd"
    print(Solution().secondHighest(s))