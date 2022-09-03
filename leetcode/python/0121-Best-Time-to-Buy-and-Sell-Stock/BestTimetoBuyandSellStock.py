from typing import List
import operator
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxEndingHere, maxSofFar = 0, 0
        for profit in map(operator.sub, prices[1:], prices):
            maxEndingHere = max(maxEndingHere + profit, profit)
            maxSofFar = max(maxSofFar, maxEndingHere)
        return maxSofFar

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
        