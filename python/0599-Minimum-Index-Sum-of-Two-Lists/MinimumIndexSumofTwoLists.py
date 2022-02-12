from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {value: index for index, value in enumerate(list1)}
        best, ans = float('inf'), []
        for index, value in enumerate(list2):
            if value not in dict: 
                continue
            if index + dict[value] < best:
                best = index + dict[value]
                ans = [value]
            elif index + dict[value] == best:
                ans.append(value)
        return ans

if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(Solution().findRestaurant(list1, list2))  