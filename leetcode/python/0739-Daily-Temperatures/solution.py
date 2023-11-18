from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return False # type: ignore

        stack, result = [], [0] * len(temperatures)
        for index, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                top_index = stack.pop()
                result[top_index] = index - top_index
            stack.append(index)
        return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))
