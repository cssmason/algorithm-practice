class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start_index, combination, res):
            if target == 0:
                res.append(combination[:])
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i] > target:
                    return
                combination.append(candidates[i])
                dfs(candidates, target - candidates[i], i, combination, res)
                combination.pop()

        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)

        return res