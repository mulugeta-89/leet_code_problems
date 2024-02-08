class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        prefix_dict = {0:1}
        for i in range(len(nums)):
            sums += nums[i]
            if sums-k in prefix_dict:
                count += prefix_dict[sums-k]
            prefix_dict[sums] = prefix_dict.get(sums, 0)+1
        return count