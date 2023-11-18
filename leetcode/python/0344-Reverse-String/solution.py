from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # solution 1:
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s  # type: ignore

        # solution 2:
        # stack = []
        # for c in s:
        #     stack.append(c)
        # i = 0
        # while stack:
        #     s[i] = stack.pop()
        #     i += 1

        # solution 3:
        # def reverse(left, right):
        #     if left < right:
        #         s[left], s[right] = s[right], s[left]
        #         reverse(left+1, right-1)
        # reverse(0, len(s)-1)


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s))
