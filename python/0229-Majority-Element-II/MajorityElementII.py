class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, count1, num2, count2 = None, 0, None, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
        
        res = []
        if count1 > len(nums) // 3:
            res.append(num1)
        if count2 > len(nums) // 3:
            res.append(num2)
        
        return res