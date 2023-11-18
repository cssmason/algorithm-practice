class Solution:
    def minOperations(self, s: str) -> int:
        zero_one_sum, n = 0, len(s)
        for i in range(n):
            zero_one_sum += 1 if i % 2 != int(s[i]) else 0
        return min(zero_one_sum, n - zero_one_sum)


if __name__ == '__main__':
    s = "0100"
    print(Solution().minOperations(s))
