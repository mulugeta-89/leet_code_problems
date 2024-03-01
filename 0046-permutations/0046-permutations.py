class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        k = len(nums)
        def backtrack(path):
            if len(path) == k:
                sol.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return sol
        