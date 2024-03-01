class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()
        def backtrack(start,target,path):
            if target == 0:
                sol.append(path[:])
                return
            for i in range(start, len(candidates)):
                if target-candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(i, target-candidates[i], path)
                    path.pop()
        backtrack(0, target, [])        
        return sol