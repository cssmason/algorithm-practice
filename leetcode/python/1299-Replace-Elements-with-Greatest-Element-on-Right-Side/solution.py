from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(Solution().replaceElements(arr))
