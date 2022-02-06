class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

if __name__ == '__main__':
    s = "paper"
    t = "title"
    print(Solution().isIsomorphic(s, t))
