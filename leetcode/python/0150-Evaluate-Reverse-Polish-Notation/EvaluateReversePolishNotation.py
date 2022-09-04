from typing import List
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(int(operators[token](first, second)))
        return stack.pop()
        
if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    print(Solution().evalRPN(tokens))