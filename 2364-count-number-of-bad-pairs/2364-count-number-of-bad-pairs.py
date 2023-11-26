class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dicti = collections.defaultdict(int)
        goodpair = 0
        diff = 0
        for i in range(len(nums)):
            diff = nums[i]-i
            goodpair += dicti[diff]
            dicti[diff] += 1
        total_pair = (n*(n-1))/2
        return int(total_pair-goodpair)
        