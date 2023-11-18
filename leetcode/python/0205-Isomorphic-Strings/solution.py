class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # solution 1
        mapST, mapTS = {}, {}
        for char1, char2 in zip(s, t):
            if ((char1 in mapST and mapST[char1] != char2) or
               (char2 in mapTS and mapTS[char2] != char1)):
                return False
            mapST[char1] = char2
            mapTS[char2] = char1
        return True

        # solution 2
        # return len(set(s)) == len(set(t)) == len(set(zip(s,t)))


if __name__ == '__main__':
    s = "paper"
    t = "title"
    print(Solution().isIsomorphic(s, t))
