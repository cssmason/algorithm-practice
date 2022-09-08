class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up, down, res = 0, 0, 0
        for i in range(1, len(arr)):
            if down > 0 and arr[i-1] < arr[i] or arr[i-1] == arr[i]:
                up, down = 0, 0
            up += arr[i-1] < arr[i]
            down += arr[i-1] > arr[i]
            if up and down:
                res = max(res, up + down + 1)
        return res