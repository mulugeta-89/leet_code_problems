class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        nums_dict = dict(Counter(nums))
        for key in nums_dict.keys():
            if nums_dict[key] == n:
                return key
        
        