class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(root, path):
            sol.append(path[:])
            for i in range(root, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return sol
        