class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        sol_arr = []
        for item in nums_dict.keys():
            if nums_dict[item] > len(nums)//3:
                sol_arr.append(item)
        return sol_arr