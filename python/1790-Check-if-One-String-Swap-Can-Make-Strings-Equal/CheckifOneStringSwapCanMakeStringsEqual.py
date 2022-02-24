class Solution:
    # Solution 1
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_index.append(i)
                if len(diff_index) > 2:
                    return False
        if (len(diff_index) == 0):
            return True
        elif (len(diff_index) != 2):
            return False
        return s1[diff_index[0]] == s2[diff_index[1]] and s1[diff_index[1]] == s2[diff_index[0]]

    # Solution 2
    # def areAlmostEqual(self, s1: str, s2: str) -> bool:
    #     diff = [(char1, char2) for char1, char2 in zip(s1, s2) if char1 != char2]
    #     return (len(diff) == 0 or (len(diff) == 2 and diff[0][::-1] == diff[1]))

if __name__ == '__main__':
    s1 = "bank"
    s2 = "kanb"
    print(Solution().areAlmostEqual(s1, s2))