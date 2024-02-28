class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        sol = 0
        last_item = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > last_item:
                ops = math.ceil(nums[i]/last_item)
                last_item = nums[i] // ops
                sol += ops -1
            else:
                last_item = nums[i]
        return sol
        