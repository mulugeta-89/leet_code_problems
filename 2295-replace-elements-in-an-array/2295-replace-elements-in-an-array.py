class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dicti = {num:i for i, num in enumerate(nums)}
        for f,s in operations:
            index = dicti[f]
            nums[index] = s
            dicti[s] = index
            del dicti[f]
        return nums