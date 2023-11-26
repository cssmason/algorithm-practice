from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            pivot, p = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                nums[p], nums[right] = nums[right], nums[p]

                if p > k:
                    return quickSelec(left, p - 1)
                elif p < k:
                    return quickSelect(p + 1, right)
                else:
                    return nums[p]

        return quickSelect(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
