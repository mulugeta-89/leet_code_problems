class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxi = 0
        freq = {1:0, 0:0}
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            maxi = max(maxi, right-left+1)
        return maxi
        