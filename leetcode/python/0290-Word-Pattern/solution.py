class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # solution 1:
        # s = s.split()
        # return len(pattern) == len(s) and len(set(pattern)) == len(set(s)) == len(set(zip(pattern,s)))

        # solution 2:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        char2Word = {}
        word2Char = {}
        for c, w in zip(pattern, words):
            if c in char2Word and char2Word[c] != w:
                return False
            if w in word2Char and word2Char[w] != c:
                return False
            char2Word[c] = w
            word2Char[w] = c
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))
