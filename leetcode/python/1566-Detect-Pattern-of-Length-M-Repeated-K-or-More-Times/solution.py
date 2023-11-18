from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i+m]:
                streak += 1
            else:
                streak = 0
            if streak == m * (k-1):
                return True
        return False


if __name__ == '__main__':
    arr = [1, 2, 4, 4, 4, 4]
    m = 1
    k = 3
    print(Solution().containsPattern(arr, m, k))
