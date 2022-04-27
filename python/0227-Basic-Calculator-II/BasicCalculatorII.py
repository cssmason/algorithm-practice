class Solution:
    def calculate(self, s: str) -> int:
        # sample
        # 5 - 2 + 3*3 - 5/2
        # output result = 5 + (-2) + (3*3) + (-5/2)
        # stack = [5, -2, 9, -2]
        # output result = sum(stack)
        
        if not s:
            return '0'
        
        num, sign, stack = 0, '+', []
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                num, sign = 0, c
        return sum(stack)

if __name__ == '__main__':
    s = '5-2+3*3-5/2'
    print(Solution().calculate(s))

