from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(len(matrix) - 1):
            for c in range(len(matrix[0]) - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(Solution().isToeplitzMatrix(matrix))
