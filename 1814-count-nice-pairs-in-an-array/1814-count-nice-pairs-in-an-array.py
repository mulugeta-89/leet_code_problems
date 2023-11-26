class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dicti = collections.defaultdict(int)
        mod = 10 **9 + 7
        ans = 0
        for item in nums:
            item -= int(str(item)[::-1])
            ans += dicti[item]
            dicti[item] += 1
        return ans%mod
        