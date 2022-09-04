class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c <= stack[-1] and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

if __name__ == '__main__':
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))