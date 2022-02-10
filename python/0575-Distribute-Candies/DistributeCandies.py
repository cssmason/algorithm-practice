from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))

if __name__ == '__main__':
    candyType = [1, 1, 2, 3]
    print(Solution().distributeCandies(candyType))