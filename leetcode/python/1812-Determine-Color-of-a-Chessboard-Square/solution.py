class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return sum(map(ord, coordinates)) % 2 != 0


if __name__ == '__main__':
    coordinates = "a1"
    print(Solution().squareIsWhite(coordinates))
