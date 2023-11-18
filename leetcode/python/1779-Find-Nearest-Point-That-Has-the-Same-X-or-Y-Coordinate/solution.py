from math import inf
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        small_dist = inf
        for i in range(len(points)):
            dist = abs(points[i][0] - x) + abs(points[i][1] - y)
            if (points[i][0] == x or points[i][1] == y) and dist < small_dist:
                small_dist = dist
                res = i
        return res


if __name__ == '__main__':
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    print(Solution().nearestValidPoint(x, y, points))
