class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = 0
        nums_dict = Counter(nums)
        nums = sorted(list(set(nums)))
        for i in range(1, len(nums)):
            count += nums_dict[nums[i]] * (i-0)
        return count
        