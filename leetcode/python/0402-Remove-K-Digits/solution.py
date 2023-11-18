class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # edge case
        if len(num) <= k:
            return '0'

        stack = []
        for digit in num:
            while stack and int(stack[-1]) > int(digit) and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num, k))
