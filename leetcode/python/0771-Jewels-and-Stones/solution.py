class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        return sum(stone in jewel for stone in stones)

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))