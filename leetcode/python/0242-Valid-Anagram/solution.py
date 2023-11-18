class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
