from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        else:
            ans = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(m * n):
                src_x = i // n
                src_y = i % n
                dst_x = i // c
                dst_y = i % c
                ans[dst_x][dst_y] = mat[src_x][src_y]
            return ans


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(Solution().matrixReshape(mat, r, c))
