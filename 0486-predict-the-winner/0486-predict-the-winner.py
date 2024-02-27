class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]
            dp[l][r] = max(nums[l]-dfs(l+1, r), nums[r]-dfs(l, r-1))
            return dp[l][r]
        dfs(0, n-1)
        return dp[0][n-1] >= 0