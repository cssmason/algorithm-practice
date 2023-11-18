import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for index, value in enumerate(s):
            if counter[value] == 1:
                return index
        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
