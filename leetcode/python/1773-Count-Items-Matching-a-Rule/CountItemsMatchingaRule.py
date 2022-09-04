from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        lookup = {'type': 0, 'color': 1, 'name': 2}
        return sum(item[lookup[ruleKey]] == ruleValue for item in items)

if __name__ == '__main__':
    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(Solution().countMatches(items, ruleKey, ruleValue))