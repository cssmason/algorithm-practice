from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(c) for c in zip(*mat[::-1])]
        return False
        
if __name__ == '__main__':
    mat = [[0, 1], [1, 0]]
    target = [[1, 0], [0, 1]]
    print(Solution().findRotation(mat, target))