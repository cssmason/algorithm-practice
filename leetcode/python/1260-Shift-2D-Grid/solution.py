from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        def posToVal(r, c):
            return r * N + c

        def valToPos(v):
            return [v // N, v % N]
           
        res = [[0] * N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k) % (M * N)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
        return res


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(Solution().shiftGrid(grid, k))
