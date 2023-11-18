from typing import List
import operator


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr_sort = sorted(arr)
        arr_diff = map(operator.sub, arr_sort, arr_sort[1:])
        return len(set(arr_diff)) == 1


if __name__ == '__main__':
    arr = [3, 5, 1]
    print(Solution().canMakeArithmeticProgression(arr))
