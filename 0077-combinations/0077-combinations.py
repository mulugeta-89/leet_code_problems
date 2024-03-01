class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtrack(root, path):
            if len(path) == k:
                sol.append(path[:])
                return
            for num in range(root, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()
        backtrack(1, [])
        return sol
        

        