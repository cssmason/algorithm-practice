from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            res += buckets[i]
            if len(res) == k:
                return res
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
