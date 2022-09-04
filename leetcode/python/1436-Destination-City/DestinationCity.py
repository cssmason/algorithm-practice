from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origin, dest = map(set, zip(*paths))
        return (dest - origin).pop()

if __name__ == '__main__':
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(Solution().destCity(paths))