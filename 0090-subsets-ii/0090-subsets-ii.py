class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        def backtrack(root, path):
            if path not in sol:
                sol.append(path[:])
            for i in range(root, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return sol
        