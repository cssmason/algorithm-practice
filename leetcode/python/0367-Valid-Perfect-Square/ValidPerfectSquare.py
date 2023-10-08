class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            middle = (left+right) // 2
            if middle * middle > num:
                right = middle - 1
            elif middle * middle < num:
                left = middle + 1
            else:
                return True
        return False


if __name__ == '__main__':
    num = 16
    print(Solution().isPerfectSquare(num))
