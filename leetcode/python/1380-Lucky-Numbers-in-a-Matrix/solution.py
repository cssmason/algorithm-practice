from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = {min(r) for r in matrix}
        col_max = {max(c) for c in zip(*matrix)}
        return list(row_min & col_max)


if __name__ == '__main__':
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(Solution().luckyNumbers(matrix))
