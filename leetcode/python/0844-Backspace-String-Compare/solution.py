class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S: str) -> list:
            stack = []
            for c in S:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return build(s) == build(t)


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print(Solution().backspaceCompare(s, t))
