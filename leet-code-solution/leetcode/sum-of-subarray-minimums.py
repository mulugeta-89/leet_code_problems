class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sol = 0
        mod = 10 ** 9 + 7
        for ind, item in enumerate(arr):
            while stack and item < arr[stack[-1]]:
                j = stack.pop()
                lower = stack[-1] if stack else -1
                sol = sol + arr[j] * (ind-j) * (j-lower)
            stack.append(ind)
        while stack:
            j = stack.pop()
            lower = stack[-1] if stack else -1
            sol = sol + arr[j] * (len(arr)-j) * (j-lower)
        return sol % mod
        