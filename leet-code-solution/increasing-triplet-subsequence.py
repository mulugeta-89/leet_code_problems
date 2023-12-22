class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left_min, right_max = [0]*len(nums), [0]*len(nums)
        left_min[0] = float("inf")
        right_max[len(nums)-1] = -float("inf")

        for i in range(1, len(nums)):
            left_min[i] = min(left_min[i-1], nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            right_max[i] = max(right_max[i+1], nums[i+1])
        for i in range(1, len(nums)-1):
            if nums[i] > left_min[i] and nums[i] < right_max[i]:
                return True
        return False
        