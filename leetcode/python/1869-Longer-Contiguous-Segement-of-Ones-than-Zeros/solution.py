class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, ones = 0, 0
        max_zeros, max_ones = 0, 0
        for char in s:
            if char == '0':
                zeros += 1
                ones = 0
                max_zeros = max(max_zeros, zeros)
            else:
                zeros = 0
                ones += 1
                max_ones = max(max_ones, ones)
        return max_zeros < max_ones


if __name__ == '__main__':
    s = "1101"
    print(Solution().checkZeroOnes(s))
