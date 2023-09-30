class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index, length = len(s)-1, 0
        while s[index] == " ":
            index -= 1
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1
        return length


if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
