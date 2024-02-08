class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        nums_dict = {0:1}
        count = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums-goal in nums_dict:
                count += nums_dict[sums-goal]
            nums_dict[sums] = nums_dict.get(sums, 0)+1
        return count