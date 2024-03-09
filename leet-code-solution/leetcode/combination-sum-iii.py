class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sol_arr = []
        candidates = [1,2,3,4,5,6,7,8,9]
        def backtrack(root,target, path):
            if target == 0 and len(path) == k:
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
        backtrack(0,n, [])
        return sol_arr
        