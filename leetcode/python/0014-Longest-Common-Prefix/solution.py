from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = strs.pop()
        for index, char in enumerate(last):
            for str in strs:
                if index >= len(str) or str[index] != char:
                    return last[:index]
        return last


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
