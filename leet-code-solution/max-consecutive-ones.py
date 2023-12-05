class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxi = 0
        for item in nums:
            if item == 1:
                counter += 1
                maxi = max(maxi, counter)
            else:
                counter = 0
        return maxi