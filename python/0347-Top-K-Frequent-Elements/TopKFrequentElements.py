class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets= [[] for _ in range(len(nums) + 1)]
        
        for key, value in counts.items():
            buckets[value].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            res += buckets[i]
            if len(res) == k:
                return res
        return res