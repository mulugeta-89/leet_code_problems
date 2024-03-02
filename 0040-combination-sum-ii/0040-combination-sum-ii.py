class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol_arr = []
        candidates.sort()
        def backtrack(root,target, path):
            if target == 0:
                sol_arr.append(path[:])
                return
            for i in range(root, len(candidates)):
                if i > root and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, target-candidates[i],path)
                path.pop()
        backtrack(0,target, [])
        return sol_arr
        