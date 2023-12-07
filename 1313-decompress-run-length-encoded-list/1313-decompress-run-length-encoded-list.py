class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sol_arr = []
        for i in range(0,len(nums), 2):
            sol_arr += [nums[i+1] ] * nums[i]
        return sol_arr
        