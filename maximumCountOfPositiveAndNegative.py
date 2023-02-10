class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for item in nums:
            if item < 0:
                neg+=1
            if item > 0:
                pos += 1
        return max(pos, neg)