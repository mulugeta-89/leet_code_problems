class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        prefix_dict = {0:1}
        for i in range(len(nums)):
            sums += (nums[i]%k)
            if (sums-k)%k in prefix_dict:
                count += prefix_dict[(sums-k)%k]
            prefix_dict[sums%k] = prefix_dict.get(sums%k, 0)+1
        return count
        