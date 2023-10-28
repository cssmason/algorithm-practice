from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        # first condition: visited -> course has been added to output
        # second condition: visiting -> course not added to output, but added to cycle
        # first condition: visited -> course not added to output or cycle
        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().findOrder(numCourses, prerequisites))
