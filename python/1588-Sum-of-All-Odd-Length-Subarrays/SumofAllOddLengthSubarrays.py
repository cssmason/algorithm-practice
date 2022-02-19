from typing import List
class Solution:
# solution 1: running prefix sum - time complexity O(n^2)
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            sub = 0
            for j in range(i, n):
                sub += arr[j] 
                ans += sub if ((j - i + 1) % 2) == 1 else 0
        return ans
        
if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(Solution().sumOddLengthSubarrays(arr))